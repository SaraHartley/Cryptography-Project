from Crypto.Util.Padding import unpad # Importing the unpad function from the Crypto.Util.Padding module
from Crypto.Cipher import DES # Importing the DES cipher module from the Crypto.Cipher module

def decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB) # Creating a new DES cipher object with the specified key and mode (ECB)
    plaintext = cipher.decrypt(ciphertext) # Decrypting the ciphertext using the DES cipher object
    plaintext = unpad(plaintext, DES.block_size) # Removing any padding from the decrypted plaintext using the unpad function
    return plaintext # Returning the decrypted and unpadded plaintext

key = b'secret_k' # Defining the key used to encrypt the ciphertext as a byte string
ciphertext = b'\x1e=Z\xa4\xae\t\x04\x02x\x17\nl\xcb\xd7tVVaZ\xfeV\x1e,\xa0\xc4de>\x19~e\x98\xa8\x9ekS\xf2\xbeBE' # Defining the ciphertext to be decrypted as a byte string
plaintext = decrypt(key, ciphertext) # Decrypting the ciphertext using the specified key and storing the result in the plaintext variable

print(plaintext) # Printing the decrypted plaintext to the console