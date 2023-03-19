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
min_time, avg_time = time_func(decrypt_caesar, "Once upon a time, in a world ruled by technology, there was a brilliant programmer named Max who had a knack for solving complex problems. Max's reputation had spread far and wide, and he had become known as the '@Mastermind!' because of his ability to create incredible software solutions. One day,Max received a message from an unknown sender. The message contained a series of numbers and special characters that seemed to be a code. Max was intrigued and decided to crack the code. After over 40 weeks of working 80 hours on the code, Max discovered that the message was from a mysterious organization that was looking for someone with his skills. They wanted him to create a program that would change the world forever. Max was excited by the challenge and accepted the organization's offer. He worked tirelessly on the program, putting in many sleepless nights to make sure it was perfect. Finally, the day arrived when Max completed the program and presented it to the organization. They were amazed by Max's work and declared him a genius. From that day on, Max became known as the 'Mastermind of the Tech World,' and his legacy lived on for generations to come.")

# Print the minimum time taken, the average time per call, and the total time taken
print(f"Minimum time taken: {min_time:.6f} seconds")
print(f"Average time per call: {avg_time:.10f} seconds")
print(f"Total time taken for 5 calls: {avg_time * 5:.6f} seconds")