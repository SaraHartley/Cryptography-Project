"""
Decryption algorithm for caesar cipher, this is a brute force approach that tests every key from 1-25. You then manually inspect the answers to provide the one which makes the most sense.
"""
def decrypt_caesar(ciphertext):
    result = ""
    for key in range(1, 26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shift = ord(char) + key
                if char.islower():
                    if shift > ord('z'):
                        shift -= 26
                    result += chr(shift)
                elif char.isupper():
                    if shift > ord('Z'):
                        shift -= 26
                    result += chr(shift)
                else:
                    if shift > ord('0'):
                        shift -= 10
                    result += chr(shift)
            else:
                result += char
        print("Key #{}: {}".format(key, result))

ciphertext = "Fyyfhp Wtrj fy < gjktwj Eee!"
decrypt_caesar(ciphertext)