import sys
import rzpipe
import base64
from Crypto.Cipher import ARC4

decryption_function = 0x00422f70
key_addr = 0x0042a074

# Standalone with filename as argument, otherwise interactively within rizin/cutter
if len(sys.argv) == 2:
    pipe = rzpipe.open(sys.argv[1])
else:
    pipe = rzpipe.open()

pipe.cmd('aa')

# Read key from memory (pszj = print string zeroterminated and parse json)
key = pipe.cmdj('pszj @ %s' % key_addr)['string']
print("Key: " + key)
print("--------------------------------------------------")

# Iterate references to the decryption function
for xref in pipe.cmdj('axtj %d' % decryption_function):
 
    # Find argument push before function call xref (print opcode before opcode @ address)
    argument_push = pipe.cmdj('pdj -1 @ %d' % (xref['from']))

    # Get address of encrypted string
    encrypted_string_addr = argument_push[0]['opcode'][5:]
    
    # Read encrypted string from memory (pszj = print string zeroterminated and parse json)
    encrypted_string = pipe.cmdj('pszj @ %s' % encrypted_string_addr)['string']
        
    # Decode and decrypt
    rc4 = ARC4.new(key.encode("utf8"))
    decrypted_string = rc4.decrypt(base64.b64decode(encrypted_string))
    
    print(encrypted_string + " @ " + encrypted_string_addr + ": " + decrypted_string.decode("utf-8"))
    
    # Set decrypted string as comment
    pipe.cmdj('CCu %s @ %d' % (decrypted_string, xref['from']))
