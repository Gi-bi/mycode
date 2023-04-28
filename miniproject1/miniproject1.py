#!/usr/bin/env python3

import random
import getpass

dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7,'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

dict2 = {0:'n', 1:'o', 2:'p', 3:'q', 4:'r', 5:'s', 6:'t', 7:'u', 8:'v', 9:'w', 10:'x', 11:'y', 12:'z', 13:'a', 14:'b', 15:'c', 16:'d', 17:'e', 18:'f', 19:'g', 20:'h', 21:'i', 22:'j', 23:'k', 24:'l', 25:'m'}

while True:

    user_input = getpass.getpass("Tell me a secret: \n\n").lower()

    def encrypt(user_input, shift):#random shift
        secret = '' #an empty string that holds the encrypted message
        for char in user_input:
            if(char.isalpha()): #is the user input in the alphabet
                other = (dict1[char] + shift ) % 26 #a variable other in dict2 to key 0-25 by wrapping back to 0
                secret += dict2[other]
            else:
                secret += char
    
        return secret

    #rot function to initiate the code
    def rot(user_input):
        shift = random.randint(1,14)
        result = encrypt(user_input, shift)
        print(result)
    rot(user_input)

    play_again = input("Any more secrets? [y/n]\n")

    if (play_again == 'n'):
        print()
        print("Your secret is safe with me")
        break

