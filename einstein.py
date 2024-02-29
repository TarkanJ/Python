# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Einstein's most famous equation
# created by @Martino 28th february 2024

# E = represents energy (measured in Joules)
# m = represents mass (measured in kilograms)
# c = represents the speed of light (measured approximately as 300000000 meters per second)
# Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent

# just in case :)))
import math

# BRUTAL NUMBER! :D - zero decimal digit
c2 = float(pow(300000000,2))
print(f"\n{c2:.0f}\n")

# Print 1000-separators commas
lightInt = int(c2)
print(f"{lightInt:,d}\n")

# Another 1000-separators, more likely C or JAVA style :)
separator = '{:,.2f}'.format(lightInt)
print(separator)

# input mass in kilograms
mass = input("input a mass(kg) m: ")
m = float(mass)

# Einstein most famous equation :)
E = m*c2
Energy = int(E)

# print(f"Energy in(J): {E:.3f}")
print(f"\n{Energy:,d}\n")


# TEST
value = 4.5e+17
# scientific format is converted to decimal
# with precision 6 decimal digit
print(f"{value:.6f}\n")

# Problems with BIG NUMBERS? Here it is: ;)
"""
One million = 1×106
One billion = 1×109
One trillion = 1×1012
One quadrillion = 1×1015
One quintillion = 1×1018
One sextillion = 1×1021
One septillion = 1×1024
One octillion = 1×1027
One nonillion = 1×1030
One decillion = 1×1033
One undecillion = 1×1036
One duodecillion = 1×1039
One tredecillion = 1×1042
One quattuordecillion = 1×1045
One quindecillion = 1×1048
One sexdecillion = 1×1051
One septemdecillion = 1×1054
One octodecillion = 1×1057
One novemdecillion = 1×1060
One vigintillion = 1×1063
One unvigintillion (or vigintunillion) = 1×1066
One duovigintillion (or vigintiduoillion) = 1×1069
One trevigintillion (or vigintitrillion) = 1×1072
One quattuorvigintillion (or vigintiquadrillion) = 1×1075
One quinvigintillion (or vigintiquintrillion) = 1×1078
One sexvigintillion (or vigintisextillion) = 1×1081
One septvigintillion (or vigintiseptillion) = 1×1084
One octovigintillion (or vigintoctillion) = 1×1087
One nonvigintillion (or vigintinonillion) = 1×1090
One trigintillion = 1×1093
One untrigintillion = 1×1096
One duotrigintillion = 1×1099
Ten-duotrigintillion = googol = 1×10100
"""
