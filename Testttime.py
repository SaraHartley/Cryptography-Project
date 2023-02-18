import time

def time_func(func, *args, **kwargs):
    times = []
    for i in range(5):
        start_time = time.monotonic()
        func(*args, **kwargs)
        end_time = time.monotonic()
        times.append(end_time - start_time)

    return min(times), sum(times) / len(times)

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


        # Wrap around the key if it exceeds the range of possible keys
        if key >= 25:
            key -= 26
    return candidate_plain_text

# Test the speed of my_function by calling it 5 times with your input
min_time, avg_time = time_func(decrypt_caesar, "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.")

# Print the minimum time taken, the average time per call, and the total time taken
print(f"Minimum time taken: {min_time:.6f} seconds")
print(f"Average time per call: {avg_time:.10f} seconds")
print(f"Total time taken for 5 calls: {avg_time * 5:.6f} seconds")