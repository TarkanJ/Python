import random
import os

# RussianRouletteGame

number = random.randint(1, 10)

guess = input("Guess a number between 1 a 10: ")
guess = int(guess)

if guess == number:
    print("You Won! 👍 \n")
else:
    print("\n Neuhodls, voe! 😄")
# print("\n Deleting C:\Windows\System32 in progress...")

# bacha na to, co to dělá!!!
# OPRAVDU TO FUNGUJE !!! 💩
# os.remove("C:\Windows\System32")
# os.remove("D:\Downloads\IoankaKravicka.txt")
