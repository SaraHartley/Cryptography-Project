# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:54:22 2023

SE231 RSA encryption
lmit string length to 215

@author: Sarah
"""
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import time
def test_function_speed(func,func2, *args, **kwargs):
    """Test the speed of a function by running it five times and printing the minimum time taken,
    average time per call, and total time (per 5 calls).

    Args:
        func (callable): The function to be tested.
        *args: Positional arguments to be passed to the function.
        **kwargs: Keyword arguments to be passed to the function.
    """
    times = []
    times_decrypt = []
    for i in range(5):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
        
        start_time_decrypt = time.perf_counter()
        func2(*args, **kwargs)
        end_time_decrypt = time.perf_counter()
        times_decrypt.append(end_time_decrypt - start_time_decrypt)

    print("Encryption:")    
    print("Minimum time taken: {:.6f} seconds".format(min(times)))
    print("Average time per call: {:.6f} seconds".format(sum(times) / len(times)))
    print("Total time (per 5 calls): {:.6f} seconds".format(sum(times)))
    print()
    
    print("Decryption:")
    print("Minimum time taken: {:.6f} seconds".format(min(times_decrypt)))
    print("Average time per call: {:.6f} seconds".format(sum(times_decrypt) / len(times_decrypt)))
    print("Total time (per 5 calls): {:.6f} seconds".format(sum(times_decrypt)))
    print()


def encrypt_rsa(message):
    from Crypto.PublicKey import RSA

    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)
    file_out.close()
    
    public_key = key.publickey().export_key()
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)
    file_out.close()
    
    #encrypt the data
    data = message.encode("utf-8")
    file_out = open("encrypted_data.bin", "wb")
    
    #get receiver key
    recipient_key = RSA.import_key(open("receiver.pem").read())
    session_key = get_random_bytes(16)
    
    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    
    #encrypt
    ciphertext = cipher_rsa.encrypt(data)
    print(ciphertext)
    print()


    # Load the private key from a file
    with open('private.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())
    
    # Create a cipher object for decrypting with RSA
    cipher_rsa = PKCS1_OAEP.new(private_key)
    
    # Encrypted message to be decrypted
    encrypted_message = ciphertext
    
    # Decrypt the message
    decrypted_message = cipher_rsa.decrypt(encrypted_message)
    
    # Print the decrypted message
    print(decrypted_message)

if __name__ == "__main__":
    test_function_speed(encrypt_rsa,decrypt_rsa,"Once upon a time, in a world ruled by technology, there was a brilliant programmer named Max who had a knack for solving complex problems. Max's reputation had spread far and wide, and he had become known as \"@\".")    
    test_function_speed(encrypt_rsa,decrypt_rsa,"It was the year 2021, and the world was in a state of chaos. The pandemic had taken its toll on everyone, and people were struggling to stay positive. But then, a group of volunteers came together.")
    test_function_speed(encrypt_rsa,decrypt_rsa,"There was a young entrepreneur named Emily who had a dream of creating a million-dollar business. She had just turned 22 and was determined to make her dream a reality. Emily had a business plan she believed in.")
    test_function_speed(encrypt_rsa,decrypt_rsa,"It was a dark and stormy night, and the clock had just struck 3 am. John had been working on his novel for hours, and he was starting to feel like he was losing his mind. Suddenly, he heard a knock at the door.")
    test_function_speed(encrypt_rsa,decrypt_rsa,"Maria was a passionate activist who was determined to make a difference in the world. She started a movement called \"#SaveTheOceans!\", and she spent every waking moment campaigning for cleaner seas.")
    test_function_speed(encrypt_rsa,decrypt_rsa,"Max was a thrill-seeker who loved nothing more than jumping out of airplanes. He had done it hundreds of times, and he had never felt more alive. One day, Max decided to do something truly daring.")
    test_function_speed(encrypt_rsa,decrypt_rsa,"It was the year 2042, and the world had changed. People had started to colonize Mars, and there were robots everywhere. Emma was a scientist who had just discovered a new element, which she called \"X@9!\".")
    test_function_speed(encrypt_rsa,decrypt_rsa,"It was the year 2020, and the world was facing an unprecedented crisis. The COVID-19 pandemic had swept across the globe, and people were struggling to adapt to a new way of life.")
    test_function_speed(encrypt_rsa,decrypt_rsa,"Mark was a competitive athlete who had been training for years to compete in the 2024 Olympics. He had just turned 30, and he knew that this would be his last chance to win a gold medal.")
    test_function_speed(encrypt_rsa,decrypt_rsa,"Sophie was a hacker who had been working on a project for months. She had discovered a vulnerability in a major software program, and she was determined to exploit it. Sophie spent countless hours writing code.")