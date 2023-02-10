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
                else:
                    if shift > ord('Z'):
                        shift -= 26
                    result += chr(shift)
            else:
                result += char
        print("Key #{}: {}".format(key, result))

ciphertext = "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
decrypt_caesar(ciphertext)