import random


def main():
    score = 0
    level = get_level()
    print(level)

    for _ in range (10):
        if generate_integer(level):
            score += 1
    print("Your score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter a positive integer from range 1-3...")
        except ValueError:
            print("Please insert a valid positive integer...")


def generate_integer(level):
    # Sets a range on a level
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    sum_result = x + y

    for _ in range(3):  # 3 attemps for correct answer
        try:
            answer = int(input(f"{x} + {y} = ").strip())
            if answer == sum_result:
                return True  # Correct answer raise a score
            else:
                print("EEE")  # Wrong asnwer
        except ValueError:
            print("Please insert a valid integer...")

    print("Correct answer was:", sum_result)  # If all attemps were wrong
    return False  # Returns a "False", if all attemps were wrong


if __name__ == "__main__":
    main()
