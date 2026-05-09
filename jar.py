class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self._capacity = capacity  # Maximální kapacita nádoby
        self._size = 0  # Aktuální počet cookies v nádobě

    def __str__(self):
        return f"{'🍪' * self._size}"  # Vizualizace cookies jako emoji

    def deposit(self, n):
        """
        Přidá 'n' cookies do nádoby.
        """
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._size + n > self._capacity:
            raise ValueError("Cannot exceed capacity of the jar.")
        self._size += n

    def withdraw(self, n):
        """
        Odebere 'n' cookies z nádoby.
        """
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        """
        Vrací maximální kapacitu nádoby.
        """
        return self._capacity

    @property
    def size(self):
        """
        Vrací aktuální počet cookies v nádobě.
        """
        return self._size


def main():
    jar = Jar()  # Výchozí kapacita je 12
    print("Welcome to the Cookie Jar!")
    while True:
        print(f"\nCurrent jar: {jar}")
        print(f"Cookies in jar: {jar.size}/{jar.capacity}")
        print("1. Deposit cookies")
        print("2. Withdraw cookies")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                n = int(input("How many cookies do you want to deposit? "))
                jar.deposit(n)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                n = int(input("How many cookies do you want to withdraw? "))
                jar.withdraw(n)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
