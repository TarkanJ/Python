# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# created @Ing.Martino,february import emoji

# import emoji module for Python
# pokud neni -> apt-get install pip -> pip install emoji
import emoji

smiley = str("hello :)")
hovno = str("hovno")

# vstup pro smajliky
users_in = input()
user_in = str(users_in)

if user_in == smiley:
    print("hello \N{slightly smiling face}")
elif user_in == hovno:
    print("💩 \n")
else:
    print("😕 \n")
    
"""
print(emoji.emojize(":grinning_face_with_big_eyes:"))
print(emoji.emojize(":winking_face_with_tongue:"))
print(emoji.emojize(":zipper-mouth_face:"))
"""
