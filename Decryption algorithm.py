"""
Decryption algorithm for caesar cipher, this is a brute force approach that tests every key from 1-25. You then manually inspect the answers to provide the one which makes the most sense.
"""
def decrypt_caesar(cipher_text):
    for key in range(26):
        candidate_plain_text = ""
        for char in cipher_text:
            if char.isalpha():
                shifted_char = ord(char) - key
                if char.isupper():
                    if shifted_char < ord('A'):
                        shifted_char += 26
                else:
                    if shifted_char < ord('a'):
                        shifted_char += 26
                candidate_plain_text += chr(shifted_char)
            elif char.isdigit():
                shifted_digit = ord(char) - key
                if shifted_digit < ord('0'):
                    shifted_digit += 10
                candidate_plain_text += chr(shifted_digit)
            else:
                candidate_plain_text += char
        print(f"Key = {key:2} | Plain text = {candidate_plain_text}")

        # Wrap around the key if it exceeds the range of possible keys
        if key >= 25:
            key -= 26


ciphertext = "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
decrypt_caesar(ciphertext)