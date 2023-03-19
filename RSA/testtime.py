from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time


def test_decrypt():
    # Load the private key from a file
    with open('private_key.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())

    # Create a cipher object for decrypting with RSA
    cipher_rsa = PKCS1_OAEP.new(private_key)

    # Encrypted message to be decrypted
    encrypted_message = b'\x8f\x14\xf3\x80\x03\xfe\x96\x8b\x35\x5c\x75\x3a\x3d\x8a\x7b\xe4\x75\x77\xad\x4c\x4f\x11\xea\xed\xb9\xfb\xeb\x8b\x56\x12\xeb\xd1\x7e\x03\x50\x99\xcc\x75\x91\x3a\x7f\x45\x23\xea\x75\x0c\xad\x7e\x4f\x4e\x6a\x9b'

    # Measure the time taken to decrypt the message 5 times
    times = []
    for i in range(5):
        start_time = time.time()
        decrypted_message = cipher_rsa.decrypt(encrypted_message)
        end_time = time.time()
        times.append(end_time - start_time)

    # Calculate and return the minimum, average, and total times
    min_time = min(times)
    avg_time = sum(times) / len(times)
    total_time = sum(times)

    return min_time, avg_time, total_time


min_time, avg_time, total_time = test_decrypt()
print(f"Minimum time: {min_time} seconds")
print(f"Average time: {avg_time} seconds")
print(f"Total time: {total_time} seconds")
