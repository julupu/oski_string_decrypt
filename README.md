# oski_string_decrypt

rzpipe script to decrypt strings from Oski Stealer. Currently contains hardcoded addresses. 

Blogpost: https://julian-wolf.eu/blog/oskistealer

Script can be run standalone from commandline or in the context of rizin/cutter.

## Standalone

    .\oski_string_decrypt.py file.exe

## Rizin

    rizin.exe file.exe
    . oski_string_decrypt.py
 

The comments are added at every function call for the decryption function:

![image](https://user-images.githubusercontent.com/5237525/174033435-837059f9-00a8-44ad-9bbb-93e7b3cc70cb.png)


## Cutter

Similar to Rizin, you open the console and run the script

![image](https://user-images.githubusercontent.com/5237525/174033681-bde0a793-8eb2-485c-ac49-a826cd85f987.png)
