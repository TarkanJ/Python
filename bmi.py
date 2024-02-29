# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# BMI Calculator --- created by @Martino in february 2024 ---

# imported math library just for case
import math

# druha mocnina cisla 3
# print(pow(3,2))

# input in centimeters 
height = input("height(cm): \n")

# input number tranformations
pom = float(height)
h = pow((pom/100),2)
# print(h)

# weight in kilograms
weight = input("weight(kg): \n")

w = float(weight)
# print(w)

# rounded to 3 decimal digit
BMI = round(w / h, 3)
print("BMI:", BMI)
