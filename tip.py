def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip("$"))
    percent = percent_to_float(input("What percentage would you like to tip? ").strip("%"))

#  number = text.strip("$")  # removes a "$"sign from the beginning or from the end of string
#  print(number)  # prints: 50

    dollars_to_float(dollars)
    percent_to_float(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}\n")


def dollars_to_float(d):
    # TODO
    d = float(d)
    return d


def percent_to_float(p):
    # TODO
    p = float(p)
    return p/100


main()
