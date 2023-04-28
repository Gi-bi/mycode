import random

# Define the game board
suspects = ["Colonel Mustard", "Miss Scarlet", "Professor Plum", "Mr. Green", "Mrs. Peacock", "Mrs. White"]
weapons = ["Candlestick", "Knife", "Lead Pipe", "Revolver", "Rope", "Wrench"]
locations = ["Ballroom", "Billiard Room", "Conservatory", "Dining Room", "Hall", "Kitchen", "Library", "Lounge", "Study"]

# Generate the solution to the murder
solution = (random.choice(suspects), random.choice(weapons), random.choice(locations))

# Define a function to check a guess
def check_guess(guess):
    correct = []
    incorrect = []
    for i in range(3):
        if guess[i] == solution[i]:
            correct.append(guess[i])
        elif guess[i] in suspects and solution[0] != guess[i]:
            incorrect.append(guess[i])
        elif guess[i] in weapons and solution[1] != guess[i]:
            incorrect.append(guess[i])
        elif guess[i] in locations and solution[2] != guess[i]:
            incorrect.append(guess[i])
    return (correct, incorrect)

# Play the game
print("Welcome to Clue!")
while True:
    print(suspects)
    guess_suspect = input("Enter your guess for the suspect: ")
    print(weapons)
    guess_weapon = input("Enter your guess for the weapon: ")
    print(locations)
    guess_location = input("Enter your guess for the location: ")
    guess = (guess_suspect, guess_weapon, guess_location)
    result = check_guess(guess)
    print("Correct elements:", result[0])
    print(solution)
    print("Incorrect elements:", result[1])
    if guess == solution:
        print("Congratulations! You have solved the murder.")
        break

