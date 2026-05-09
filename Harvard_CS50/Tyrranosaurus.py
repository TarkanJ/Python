import cowsay
import sys

"""
Vykresli Kravicku, T-Rexe, nebo jina zviratka :)
"""

# pokud jsou parametry prikazoveho radku dva...
# if len(sys.argv) == 2:
# cowsay.cow("Hello, " + sys.argv[1])

# cowsay.trex("Hello, " + userInput + ", I'm gonna eat You alive!!! :D")
# cowsay.pig("Hello, " + userInput + ", U Are such a...!")

def main():
    userInput = input("What's your name? ")
    choice = int(input("Choose a number 1 or 2: "))
    if choice == 1:
        kravicka(userInput)
    elif choice == 2:
        Trex(userInput)


def kravicka(user_in):
    cowsay.cow("Hello, " + user_in + ", U Are such a...!")


def Trex(user_in):
    cowsay.trex("Hello, " + user_in + ", I'm gonna eat You alive!!! :D")


main()
