# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:46:14 2023

@author: Sarah

based on https://likegeeks.com/python-caesar-cipher/
"""

def main(plaintext, shift):
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
    
    return ciphertext

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
    print("ciphertext: ",main("Attack Rome at 7 before Zzz!", 0))
    print()
    print("ciphertext: ",main("Attack Rome at 7 before Zzz!", 5))
    print()
    print("ciphertext: ",main("Attack Rome at 7 before Zzz!", -4))
    
    
    
    
    
    
    
    