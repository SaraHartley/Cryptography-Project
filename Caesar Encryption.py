# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:46:14 2023

@author: Sara

based on https://likegeeks.com/python-caesar-cipher/ and 
https://www.geeksforgeeks.org/how-to-measure-elapsed-time-in-python/
https://theasciicode.com.ar/
    
        
"""
import time
from colorama import Back,Style


def main(plaintext, shift):
    
    """
    Attempt to use Repeat
    #start timer
    #start = timeit.default_timer()
    ciphertext_a = ""
    
    #testcode = '''
    #def test():
    #    result = Encrypt_Caesar(plain)
    #'''
    t_records = timeit.repeat(lambda:Encrypt_Caesar(plaintext, shift), number=1, repeat=10)
 
    # printing the execution time
    min_m_secs = -1
    for index, exec_time in enumerate(t_records, 1):
        # printing execution time of code in microseconds
        m_secs = round(exec_time * 10 ** 6, 2)
        print(f"Time Taken: {m_secs}µs")
        if (min_m_secs < 0 or m_secs < min_m_secs):
            min_m_secs = m_secs
            print("changed: ", min_m_secs)
    #min_m_secs = round(average_m_secs,2)
    print(Back.BLUE + f"Time Taken: {min_m_secs}µs")
    print(Style.RESET_ALL)
    #print(t_records)
    """
    
    
    min_m_secs = -1
    ciphertext = ""
    times = []
    for i in range(5):
        
        #start timer
        start = time.monotonic()
    
        #run code
        ciphertext = Encrypt_Caesar(plaintext, shift)
    
        #stop timer
        stop = time.monotonic()
        execution_time = stop - start
        
        # printing execution time of code in microseconds
        m_secs = round(execution_time * 10 ** 6, 2)
        
        times.append(m_secs)
        
        if (min_m_secs < 0 or m_secs < min_m_secs):
            min_m_secs = m_secs
                
    print(f"Minimum Time Taken: {min_m_secs}µs")
    average_m_secs = sum(times)/len(times)
    print(f"Average Time Taken: {average_m_secs}µs")
    
    return ciphertext
    

def Encrypt_Caesar(plaintext, shift):
    #print("plaintext: ", plaintext)
    #print("shift: ", shift)
    
    #Declare Variables
    ciphertext = ""
    
    for letter in plaintext:    
        #1: Convert plaintext to array of numbers
        #Convert uppercase letters
        if letter.isupper():            
            #get shifted letter
            cipherletter = apply_shift(letter, shift, 'A',26)
            
            #Add converted to letter to ciphertext
            ciphertext += cipherletter
        
        #Convert lowercase letters
        elif letter.islower():
            #get shifted letter
            cipherletter = apply_shift(letter, shift, 'a',26)
            
            #Add converted to letter to ciphertext
            ciphertext += cipherletter
        
        #Convert digits
        elif letter.isdigit():
            #get shifted letter
            cipherletter = apply_shift(letter, shift, '0',10)
            
            #Add converted to letter to ciphertext
            ciphertext += cipherletter
#TODO change to check directly
        #Ascii !(33) - /(47)
        elif ((ord(letter)) > 32) and ((ord(letter))<48):
           #print("Ascii 1: "+letter + str(ord(letter)))
           #get shifted leter
           cipherletter = apply_shift(letter, shift, '!', 15)
           
           #add converted letter to ciphertext
           ciphertext += cipherletter
           
        #Ascii @(64) - :(58)
        elif ((ord(letter))>57) and ((ord(letter))<65):
            #print("Ascii 2: "+letter + str(ord(letter)))
            #get shifted leter
            cipherletter = apply_shift(letter, shift, ':', 7)
                
            #add converted letter to ciphertext
            ciphertext += cipherletter
            
        #Ascii [(91) - `(96)
        elif ((ord(letter))>90) and ((ord(letter))<97):
            #print("Ascii 3: "+letter + str(ord(letter)))
            #get shifted leter
            cipherletter = apply_shift(letter, shift, '[', 6)
                
            #add converted letter to ciphertext
            ciphertext += cipherletter
        
        #Ascii {(123) - ~(126)
        elif ((ord(letter))>122) and ((ord(letter))<127):
            #print("Ascii 4: "+letter + str(ord(letter)))
            #get shifted leter
            cipherletter = apply_shift(letter, shift, '{', 4)
                
            #add converted letter to ciphertext
            ciphertext += cipherletter
            
        else:
            ciphertext += letter
    
    return ciphertext

def apply_shift(letter, shift, test_letter,mod_num):
    #get index
    letter_index = ord(letter) - ord(test_letter)
    
    #shift index
    shifted_index = (letter_index + shift) % mod_num
    shifted_index = shifted_index + ord(test_letter)
    
    #convert index to letter
    cipherletter = chr(shifted_index)
    
    return cipherletter
    
    

if __name__ == "__main__":
    
    print(Back.CYAN,"Plaintext: test")
    print(Style.RESET_ALL)
    print("Shift: 0")
    print("Ciphertext: ",main("test", 0))
    print()
    
    print(Back.CYAN,"Plaintext: Testing Parameters")
    print(Style.RESET_ALL)
    print("Shift: 5")
    print("Ciphertext: ",main("Testing Parameters", 5))
    print()
    
    print(Back.CYAN,"Plaintext: We are Encrypting!")
    print(Style.RESET_ALL)
    print("Shift: -4")
    print("Ciphertext: ",main("We are Encrypting!", -4))
    print()
    
    print(Back.CYAN,"Plaintext: We are w0rking hard!={~")
    print(Style.RESET_ALL)
    print("Shift: -3")
    print("Ciphertext: ",main("We are w0rking hard!={~", -3))
    print()
    
    print(Back.CYAN,"Plaintext: What are we d0ing right now?!^[`")
    print(Style.RESET_ALL)
    print("Shift: 8")
    print("Ciphertext: ",main("What are we d0ing right now?!^[`", 8))
    print()
    
    print(Back.CYAN,"Plaintext: The big brown fox jumps over the lazy dog!")
    print(Style.RESET_ALL)
    print("Shift: 9")
    print("Ciphertext: ",main("The big brown fox jumps over the lazy dog!", 9))
    print()
    
    print(Back.CYAN,"Plaintext: Humpy dumpty s@t 0n the w@ll, humpty dumpty haD a great f@ll")
    print(Style.RESET_ALL)
    print("Shift: -2")
    print("Ciphertext: ",main("Humpy dumpty s@t 0n the w@ll, humpty dumpty haD a great f@ll", -2))
    print()
    
    print(Back.CYAN,"Plaintext: This is our project for Software Engineering with Crypt0raphy!?")
    print(Style.RESET_ALL)
    print("Shift: -1")
    print("Ciphertext: ",main("This is our project for Software Engineering with Crypt0raphy!?", -1))
    print()
    
    print(Back.CYAN,"Plaintext: zyxwvutsrqponmlkjihgfedcba")
    print(Style.RESET_ALL)
    print("Shift: 1")
    print("Ciphertext: ",main("zyxwvutsrqponmlkjihgfedcba", 1))
    print()
    
    print(Back.CYAN,"Plaintext: If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out.")
    print(Style.RESET_ALL)
    print("Shift: 12")
    print("Ciphertext: ",main("If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out.", 12))
    

    
    
    
    