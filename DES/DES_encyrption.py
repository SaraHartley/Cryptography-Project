# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 16:43:43 2023

DES Encryption

pip install pycryptodome
https://pycryptodome.readthedocs.io/en/latest/src/cipher/des.html
@author: Sarah
"""
from Crypto.Cipher import DES
from Crypto.Util import Padding


def main(message):
    print(message)
    key = b'-8B key-'
    cipher = DES.new(key,DES.MODE_ECB)
    plaintext = Padding.pad(message,8)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

if __name__ == "__main__":
    print(main("This is a message to encrypt at 4 pm!"))

