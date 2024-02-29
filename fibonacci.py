# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def fib(n):
    a, b = 0, 1
    print('Fibonacci sequence: ')
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(100)
