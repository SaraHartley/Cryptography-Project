import time

def test_decrypt_caesar():
    # Define a list of ciphertexts to test the function with
    ciphertexts = [" Zvwopl dhz h ohjrly dov ohk illu dvyrpun vu h wyvqlja mvy tvuaoz& Zol ohk kpzjvclylk h cbsulyhipspaf pu h thqvy zvmadhyl wyvnyht$ huk zol dhz klalytpulk av lewsvpa pa& Zvwopl zwlua jvbuaslzz ovbyz dypapun jvkl$ alzapun oly wyvnyht$ huk mpul%abupun oly zayhalnf& Mpuhssf$ aol khf hyypclk dolu zol dvbsk leljbal oly wshu& Zol pumpsayhalk aol zvmadhyl huk nhpulk hjjlzz av aol zfzalt& Zvwopl.z wyvnyht dvyrlk mshdslzzsf$ huk zol dhz hisl av zalhs chsbhisl khah myvt aol jvtwhuf& Zol mlsa h ybzo vm hkyluhspul hz zol jvtwslalk oly tpzzpvu$ ruvdpun aoha zol ohk qbza hjjvtwspzolk zvtlaopun aoha mld wlvwsl jvbsk& "]

    # Run the function five times for each ciphertext and record the times
    times = []
    for i in range(5):
        for ciphertext in ciphertexts:
            start_time = time.time()
            decrypt_caesar(ciphertext)
            end_time = time.time()
            times.append(end_time - start_time)

    # Calculate and print the minimum time taken, average time per call, and total time per five calls
    min_time = min(times)
    avg_time = sum(times) / len(times)
    total_time = sum(times)
    print(f"Minimum time taken: {min_time:.6f} seconds")
    print(f"Average time per call: {avg_time:.6f} seconds")
    print(f"Total time for five calls: {total_time:.6f} seconds")

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
            elif '!' <= char <= '/':
                # Only decrypt ASCII symbols between '!' and '@'

                shifted_char = ord(char) - shift
                if shifted_char < ord('!'):
                    shifted_char += 15  # Wrap around to the end of the range
                candidate_text += chr(shifted_char)
            elif ':' <= char <= '@':
                # Only decrypt ASCII symbols between '!' and '@'

                shifted_char = ord(char) - shift
                if shifted_char < ord(':'):
                    shifted_char += 7  # Wrap around to the end of the range
                candidate_text += chr(shifted_char)
            elif '[' <= char <= '`':
                # Only decrypt ASCII symbols between '!' and '@'

                shifted_char = ord(char) - shift
                if shifted_char < ord('['):
                    shifted_char += 6  # Wrap around to the end of the range
                candidate_text += chr(shifted_char)
            elif '{' <= char <= '~':
                # Only decrypt ASCII symbols between '!' and '@'

                shifted_char = ord(char) - shift
                if shifted_char < ord('{'):
                    shifted_char += 4  # Wrap around to the end of the range
                candidate_text += chr(shifted_char)
            else:
                candidate_text += char
        print(f"key= {shift}, Plain text = {candidate_text}")
        # Check if the candidate text looks like a valid message
        if 'the' in candidate_text.lower():
            decrypted = candidate_text
            break

    return decrypted
# Test the speed of my_function by calling it 5 times with your input
test_decrypt_caesar()

