#!/usr/bin/env python3

wordbank= ["indentation", "spaces"] 

tlgstudents= ["Brandon", "Caleb", "Cat", "Chad the Beardulous", "Chance", "Chris", "Jessica", "Jorge", "Joshua", "Justin", "Lui", "Stephen"]

wordbank.append(4)
print(wordbank)
num = int(input("Give me a number between 0-11: "))

student_name= tlgstudents.pop(num)

print(student_name)
print(tlgstudents)


