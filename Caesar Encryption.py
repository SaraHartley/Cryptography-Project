# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:46:14 2023

@author: Sara

based on https://likegeeks.com/python-caesar-cipher/ and 
https://www.geeksforgeeks.org/how-to-measure-elapsed-time-in-python/
"""
import timeit

def main(plaintext, shift):
    #start timer
    #start = timeit.default_timer()
        
    t_records = timeit.repeat(lambda: Encrypt_Caesar(plaintext, shift), number=1, repeat=1000)
 
    # printing the execution time
    average_m_secs = 0
    count = 0
    for index, exec_time in enumerate(t_records, 1):
        # printing execution time of code in microseconds
        m_secs = round(exec_time * 10 ** 6, 2)
        #print(f"Time Taken: {m_secs}µs")
        average_m_secs += m_secs
        count += 1
    average_m_secs= average_m_secs/count
    average_m_secs = round(average_m_secs,2)
    print(f"Time Taken: {average_m_secs}µs")
    
    
    
    #stop timer
    #stop = timeit.default_timer()
    #execution_time = stop - start
    #print("Program Executed in " + str(execution_time) + " seconds")
    

def Encrypt_Caesar(plaintext, shift):
    print("plaintext: ", plaintext)
    print("shift: ", shift)
    
    #Declare Variables
    ciphertext = ""
    
    for letter in plaintext:    
        #1: Convert plaintext to array of numbers
        #Convert uppercase letters
        if letter.isupper():            
            #get shifted letter
            cipherletter = apply_shift(letter, shift, 'A')
            
            #Add converted to letter to ciphertext
            ciphertext += cipherletter
        
        #Convert lowercase letters
        elif letter.islower():
            #get shifted letter
            cipherletter = apply_shift(letter, shift, 'a')
            
            #Add converted to letter to ciphertext
            ciphertext += cipherletter
        
        #Convert digits
        elif letter.isdigit():
            #get shifted letter
            cipherletter = apply_shift(letter, shift, '0')
            
            #Add converted to letter to ciphertext
            ciphertext += cipherletter
            
        else:
            ciphertext += letter
    
    print("ciphertext: ", ciphertext)
    print()

def apply_shift(letter, shift, test_letter):
    #get index
    letter_index = ord(letter) - ord(test_letter)
    
    #shift index
    shifted_index = (letter_index + shift) % 26
    shifted_index = shifted_index + ord(test_letter)
    
    #convert index to letter
    cipherletter = chr(shifted_index)
    
    return cipherletter
    
    

if __name__ == "__main__":
    main("Attack Rome at 7 before Zzz!", 0)
    print()
    main("Attack Rome at 7 before Zzz!", 5)
    print()
    main("Attack Rome at 7 before Zzz!", -4)
    
    
    
    
    
    
    
    