import tkinter as tk
from tkinter import messagebox


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative!")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies!")
        if self._size + n > self._capacity:
            raise ValueError("Not enough space in the jar!")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies!")
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar!")
        self._size -= n

    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return self._capacity


class JarGUI:
    def __init__(self, root):
        self.jar = Jar(12)  # Výchozí kapacita nádoby

        # 1. úprava kódu, přidáno: Nastavení velikosti okna a jeho umístění na střed
        self.center_window(root, 250, 300) # původně byla velikost nastavena na (root, 500, 600)

        # GUI komponenty
        self.root = root
        self.root.title("Cookie Jar")

        # Label pro zobrazení stavu nádoby
        self.status_label = tk.Label(root, text=str(self.jar), font=("Arial", 20))
        self.status_label.pack(pady=10)

        # Tlačítko pro vložení cookies
        self.deposit_label = tk.Label(root, text="Deposit cookies:")
        self.deposit_label.pack()
        self.deposit_entry = tk.Entry(root)
        self.deposit_entry.pack()
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit_cookies)
        self.deposit_button.pack(pady=5)

        # Tlačítko pro výběr cookies
        self.withdraw_label = tk.Label(root, text="Withdraw cookies:")
        self.withdraw_label.pack()
        self.withdraw_entry = tk.Entry(root)
        self.withdraw_entry.pack()
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw_cookies)
        self.withdraw_button.pack(pady=5)

        # 2. úprava kódu: Přidáno textové pole self.message_label do GUI pro zobrazování chybových hlášek:
        """
        self.message_label = tk.Label(root, text="", fg="red", font=("Arial", 12))
        self.message_label.pack(pady=10)
        """
        # Label pro kapacitu nádoby
        self.capacity_label = tk.Label(root, text=f"Capacity: {self.jar.capacity} cookies")
        self.capacity_label.pack(pady=10)

    # 1. úprava kódu, přidáno: Nastavení velikosti okna a jeho umístění na střed
    def center_window(self, root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        root.geometry(f"{width}x{height}+{x}+{y}")

    def deposit_cookies(self):
        try:
            n = int(self.deposit_entry.get())
            self.jar.deposit(n)
            self.update_status()
            self.deposit_entry.delete(0, tk.END)
            # 2. úprava kódu, přidáno: Namísto dialogového okna se chyby zobrazují v poli message_label:
            # self.message_label.config(text="")  # Vymazání chybové hlášky
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            # 2. úprava kódu, přidáno: Po úspěšném vložení nebo odebrání cookies se chybová hláška odstraní:
            # self.message_label.config(text=str(e))  # Zobrazení chyby v textovém poli

    def withdraw_cookies(self):
        try:
            n = int(self.withdraw_entry.get())
            self.jar.withdraw(n)
            self.update_status()
            self.withdraw_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_status(self):
        self.status_label.config(text=str(self.jar))


def main():
    root = tk.Tk()
    app = JarGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
