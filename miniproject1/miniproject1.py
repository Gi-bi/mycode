#!/usr/bin/env python3

import random


print("Welcome to Hangman")

with open("english.txt", "r") as file:
    answer = file.read()
    words = list(map(str, answer.split()))

    
secret_word = random.choice(words)

#Checking to see if I pulled a random word
print(secret_word)
print()
#print secret word to console but replace each character with "_ "

def hidden_word():
    hidden = ""
    for i in secret_word:
        hidden  += "_ "
    return hidden

hidden = hidden_word()


# number of attempts to increment when wrong answer
attempt = 0

#two conditions
while x in hidden and attempt <= 10:
    #Printing directions and asking the user for input 
    guess = input("You have 10 guesses. Good luck! \n")

    #using keyword "in" to check guess against the secret_word
   # if guess in secret_word:
    #    for i in range(len(secret_word)):
     #       if secret_word[i] == guess:
                

   # else:
    #    print(f"INCORRECT: You have made {attempt} guess")
     #   attempt += 1


#bank of letters already guessed
print(guess)

