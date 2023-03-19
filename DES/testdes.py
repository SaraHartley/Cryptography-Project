import time

def test_function_speed(func, *args, **kwargs):
    """Test the speed of a function by running it five times and printing the minimum time taken,
    average time per call, and total time (per 5 calls).

    Args:
        func (callable): The function to be tested.
        *args: Positional arguments to be passed to the function.
        **kwargs: Keyword arguments to be passed to the function.
    """
    times = []
    for i in range(5):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        times.append(end_time - start_time)

    print("Minimum time taken: {:.6f} seconds".format(min(times)))
    print("Average time per call: {:.6f} seconds".format(sum(times) / len(times)))
    print("Total time (per 5 calls): {:.6f} seconds".format(sum(times)))

def decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB) # Creating a new DES cipher object with the specified key and mode (ECB)
    plaintext = cipher.decrypt(ciphertext) # Decrypting the ciphertext using the DES cipher object
    plaintext = unpad(plaintext, DES.block_size) # Removing any padding from the decrypted plaintext using the unpad function
    return plaintext # Returning the decrypted and unpadded plaintext

key = b'secret_k'
ciphertext = b'\x1e=Z\xa4\xae\t\x04\x02x\x17\nl\xcb\xd7tVVaZ\xfeV\x1e,\xa0\xc4de>\x19~e\x98\xa8\x9ekS\xf2\xbeBE'

test_function_speed(decrypt, key, ciphertext)