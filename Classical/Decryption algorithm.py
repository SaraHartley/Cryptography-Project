def decrypt_caesar(cipher_text):
    decrypted = ''
    for shift in range(1, 26):
        candidate_text = ''
        for char in cipher_text:
            if char.isalpha():
                shifted_char = ord(char) - shift
                if char.isupper():
                    if shifted_char < ord('A'):
                        shifted_char += 26
                else:
                    if shifted_char < ord('a'):
                        shifted_char += 26
                candidate_text += chr(shifted_char)
            elif char.isdigit():
                # Shift digits separately from letters
                shifted_digit = (int(char) - shift) % 10
                if shifted_digit == 0:
                    shifted_digit = 10
                candidate_text += str(shifted_digit)
            else:
                candidate_text += char
        print(f"key= {shift}, Plain text = {candidate_text}")

# Check if the candidate text looks like a valid message
        if 'the' in candidate_text.lower():
            decrypted = candidate_text
             break
        return decrypted
ciphertext = "haahjr ha 14"
decrypt_caesar(ciphertext)