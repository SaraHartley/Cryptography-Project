from Crypto.Cipher import DES

# Define a function to brute force a DES encrypted ciphertext
def brute_force_decrypt(ciphertext):
    # Loop through all possible 56-bit keys
    for i in range(2**56):
        # Convert the current key to a 64-bit binary string and add null byte at the end
        key = i.to_bytes(7, byteorder='big') + b'\x00'

        # Create a new DES cipher with the current key
        cipher = DES.new(key, DES.MODE_ECB)

        # Decrypt the ciphertext using the current key and cipher
        plaintext = cipher.decrypt(ciphertext)

        # Check if the decrypted plaintext contains the word "flag"
        if b'flag' in plaintext:
            # If the plaintext contains "flag", return the key and plaintext
            return key, plaintext

    # If no key is found, return None
    return None

# Define a ciphertext to decrypt
ciphertext = b'\xfe\xf9\x8dW\x8c3\x1e\xfa@\x87\xb6\xf4\xe6\xee\xcf'

# Call the brute force decryption function on the ciphertext
result = brute_force_decrypt(ciphertext)

# Check if a key was found
if result:
    # If a key was found, print the key and decrypted plaintext
    key, plaintext = result
    print(f"Key found: {key.hex()}")
    print(f"Plaintext: {plaintext.decode()}")
else:
    # If no key was found, print an error message
    print("Could not find key")