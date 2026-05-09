# created by @Martino 26th June 2024
expression = input("Expression: ").strip()

a, operator, b = expression.split(" ")

a_nr = float(a)
b_nr = float(b)

# Initialization variable for the result
result = None

# Choosing the right operator and enumeration
if operator == '+':
    result = a_nr + b_nr
elif operator == '-':
    result = a_nr - b_nr
elif operator == '*':
    result = a_nr * b_nr
elif operator == '/':
    if b_nr == 0:
        result = "Error: Divide by Zero."
    else:
        result = a_nr / b_nr
else:
    result = "Error: Unvalid operator."

print(result)
