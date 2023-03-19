import time
from Crypto.Util.Padding import unpad # Importing the unpad function from the Crypto.Util.Padding module
from Crypto.Cipher import DES # Importing the DES cipher module from the Crypto.Cipher module
def time_func(func, *args, **kwargs):
    times = []
    for i in range(5):
        start_time = time.monotonic()
        func(*args, **kwargs)
        end_time = time.monotonic()
        times.append(end_time - start_time)

    return min(times), sum(times) / len(times)

def decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB) # Creating a new DES cipher object with the specified key and mode (ECB)
    plaintext = cipher.decrypt(ciphertext) # Decrypting the ciphertext using the DES cipher object
    plaintext = unpad(plaintext, DES.block_size) # Removing any padding from the decrypted plaintext using the unpad function
    return plaintext # Returning the decrypted and unpadded plaintext

key = b'secret_k' # Defining the key used to encrypt the ciphertext as a byte string
ciphertext = b'\x1e=Z\xa4\xae\t\x04\x02x\x17\nl\xcb\xd7tVVaZ\xfeV\x1e,\xa0\xc4de>\x19~e\x98\xa8\x9ekS\xf2\xbeBE' # Defining the ciphertext to be decrypted as a byte string
plaintext = decrypt(key, ciphertext) # Decrypting the ciphertext using the specified key and storing the result in the plaintext variable

# Test the speed of my_function by calling it 5 times with your input
min_time, avg_time = time_func(decrypt(key,ciphertext))
# Print the minimum time taken, the average time per call, and the total time taken
print(f"Minimum time taken: {min_time:.6f} seconds")
print(f"Average time per call: {avg_time:.10f} seconds")
print(f"Total time taken for 5 calls: {avg_time * 5:.6f} seconds")