# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 16:43:43 2023

DES Encryption

pip install pycryptodome
https://pycryptodome.readthedocs.io/en/latest/src/cipher/des.html
@author: Sarah
"""
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


def main(message):
    #define key
    key = b'secret_k'
    print(key)
    #define plaintext
    plaintext = str.encode(message)
    print(plaintext)
    #create cipher
    cipher = DES.new(key,DES.MODE_ECB)

    #pad 
    padded_plaintext = pad(plaintext,DES.block_size)

    #encrypt plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    print(ciphertext)

if __name__ == "__main__":
    main('This is a message to encrypt at 4 pm!')

