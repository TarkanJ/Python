"""
# Vytiskne 10x "Ahoj lidi!"

count = 0
while (count < 10):
    count = count + 1
    print(count, "Ahoj lidi!")
"""

""""
# use of range() to define a range of values
values = range(10)

# iteruje od iterate from i = 0 to i = 9
for i in values:
    print(i)
"""

# Python program to illustrate
# nested for loops in Python (vnořené cykly v Pythonu)

for i in range(1, 11):
    for j in range(i):
        print(end=' *')
    print()
