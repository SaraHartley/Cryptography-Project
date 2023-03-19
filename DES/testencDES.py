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

def encrypt_des(message):
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

test_function_speed(encrypt_des,"Once upon a time")