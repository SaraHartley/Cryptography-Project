# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 16:43:43 2023

DES Encryption

pip install pycryptodome
https://pycryptodome.readthedocs.io/en/latest/src/cipher/des.html
@author: Sarah
"""
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import time
from colorama import Back,Style

def main(plaintext):
    print(Back.CYAN,"Plaintext: " ,plaintext)
    print(Style.RESET_ALL)
    
    min_m_secs = -1
    ciphertext = ""
    times = []
    for i in range(5):
        
        #start timer
        start = time.monotonic()
    
        #run code
        ciphertext = encrypt_des(plaintext)
    
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
    print("Ciphertext: ", ciphertext)
    print()

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

if __name__ == "__main__":
    main("test")
    
    main("Once upon a time, in a world ruled by technology, there was a brilliant programmer named Max who had a knack for solving complex problems. Max's reputation had spread far and wide, and he had become known as the \"@Mastermind!\" because of his ability to create incredible software solutions. One day, Max received a message from an unknown sender. The message contained a series of numbers and special characters that seemed to be a code. Max was intrigued and decided to crack the code. After over 40 weeks of working 80 hours on the code, Max discovered that the message was from a mysterious organization that was looking for someone with his skills. They wanted him to create a program that would change the world forever. Max was excited by the challenge and accepted the organization's offer. He worked tirelessly on the program, putting in many sleepless nights to make sure it was perfect. Finally, the day arrived when Max completed the program and presented it to the organization. They were amazed by Max's work and declared him a genius. From that day on, Max became known as the \"Mastermind of the Tech World,\" and his legacy lived on for generations to come.")
    
    main("It was the year 2021, and the world was in a state of chaos. The pandemic had taken its toll on everyone, and people were struggling to stay positive. But then, a group of volunteers came together and launched a campaign called \"#SpreadLove!\". The campaign went viral, and people all over the world started sharing messages of hope and positivity. The simple act of spreading love had a profound impact, and it helped to bring people together during a difficult time.")
    
    main("There was a young entrepreneur named Emily who had a dream of creating a million-dollar business. She had just turned 22 and was determined to make her dream a reality. Emily had a business plan that she believed in, and she worked tirelessly to make it happen. Finally, after years of hard work, Emily's business took off, and she became a millionaire at the age of 28. She celebrated by throwing a party with 99 of her closest friends, and they all cheered her on as she made a speech thanking them for their support.")
    
    main("It was a dark and stormy night, and the clock had just struck 3 am. John had been working on his novel for hours, and he was starting to feel like he was losing his mind. Suddenly, he heard a knock at the door. He opened it to find a stranger standing in front of him. The stranger handed him a note that said, \"You have exactly 7 days to finish your novel, or else.\" John was shaken but also motivated. He worked harder than ever and finished his novel in 6 days. The book became a bestseller and John became a successful author, but healways wondered who had sent him that note.")
    
    main("Maria was a passionate activist who was determined to make a difference in the world. She started a movement called \"#SaveTheOceans!\", and she spent every waking moment campaigning for cleaner seas. Maria's message resonated with people all over the world, and she became a symbol of hope for the future. She organized beach cleanups, spoke at conferences, and even swam from one end of the ocean to the other. Thanks to her efforts, the oceans began to recover, and marine life flourished once again.")
    
    main("Max was a thrill-seeker who loved nothing more than jumping out of airplanes. He had done it hundreds of times, and he had never felt more alive. One day, Max decided to do something truly daring. He jumped out of a plane at an altitude of 9,000 feet, with nothing but a parachute and his own bravery. The wind whipped past him as he fell, and he felt like he was flying. Finally, he pulled the cord on his parachute and floated gently to the ground. Max felt invincible, and he knew that he would never stop chasing adventure.")
    
    main("It was the year 2042, and the world had changed. People had started to colonize Mars, and there were robots everywhere. Emma was a scientist who had just discovered a new element, which she called \"X@9!\". It had the power to revolutionize the world, but it was also highly unstable. Emma worked tirelessly to find a way to stabilize the element, and after many failed attempts, she finally succeeded. The world was never the same again, and Emma became known as the \"Mother of X@9!\"")
    
    main("It was the year 2020, and the world was facing an unprecedented crisis. The COVID-19 pandemic had swept across the globe, and people were struggling to adapt to a new way of life. But there was one group of people who rose to the challenge and fought back against the virus. The frontline workers, who risked their lives every day, became the heroes of the pandemic. They worked tirelessly to save lives, and their bravery inspired a sense of unity and hope in a time of great uncertainty.")
    
    main("Mark was a competitive athlete who had been training for years to compete in the 2024 Olympics. He had just turned 30, and he knew that this would be his last chance to win a gold medal. Mark worked harder than ever, pushing himself to his limits. He ran 10 miles every day, lifted weights for 8 hours a week, and practiced his sport for 9 hours a day. Finally, the day of the competition arrived, and Mark gave it his all. He ran faster, lifted more, and performed better than ever before. In the end, he won the gold medal, and he knew that all of his hard work had been worth it.")
    
    main("Sophie was a hacker who had been working on a project for months. She had discovered a vulnerability in a major software program, and she was determined to exploit it. Sophie spent countless hours writing code, testing her program, and fine-tuning her strategy. Finally, the day arrived when she would execute her plan. She infiltrated the software and gained access to the system. Sophie's program worked flawlessly, and she was able to steal valuable data from the company. She felt a rush of adrenaline as she completed her mission, knowing that she had just accomplished something that few people could.")
    

