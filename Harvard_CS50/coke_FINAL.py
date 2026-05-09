""" Suppose that a machine sells bottles of Coca-Cola (Coke)
for 50 cents and only accepts coins in these denominations:
    25 cents, 10 cents, and 5 cents.
"""

amountDue = 50
print("Amount Due: 50")

while amountDue > 0:
    cokeMachine = int(input("Insert Coin: ").strip())

    if cokeMachine in [5, 10, 25]:
        amountDue -= cokeMachine
        if amountDue > 0:
            print(f"Amount Due: {amountDue}")
        else:
            print(f"Change Owed: {-amountDue}")
    else:
        print(f"Amount Due: {amountDue}")
