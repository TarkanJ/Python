import customtkinter as ctk
from loan_calculator import LoanCalculator
from PIL import Image  # Knihovna pro práci s obrázky

# Nastavení vzhledu aplikace
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class LoanApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x600")
        self.title("Loan Calculator")

        # Načtení a zobrazení obrázku
        # self.image = ctk.CTkImage(light_image=Image.open("Pocitadlo.png"), size=(100, 100))
        # self.label_image = ctk.CTkLabel(self, image=self.image, text="")
        # self.label_image.pack(pady=5)

        # Nadpis
        self.label_title = ctk.CTkLabel(self, text="Loan Calculator", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=10)

        # Vstupy
        self.label_amount = ctk.CTkLabel(self, text="Loan Amount:")
        self.label_amount.pack()
        self.entry_amount = ctk.CTkEntry(self)
        self.entry_amount.pack(pady=5)

        self.label_period = ctk.CTkLabel(self, text="Period (Years):")
        self.label_period.pack()
        self.entry_period = ctk.CTkEntry(self)
        self.entry_period.pack(pady=5)

        self.label_rate = ctk.CTkLabel(self, text="Interest Rate (%):")
        self.label_rate.pack()
        self.entry_rate = ctk.CTkEntry(self)
        self.entry_rate.pack(pady=5)

        # Tlačítko pro výpočet
        self.button_calculate = ctk.CTkButton(self, text="Calculate", command=self.calculate)
        self.button_calculate.pack(pady=15)

        # Výstupy
        self.label_result = ctk.CTkLabel(self, text="Monthly Payment:")
        self.label_result.pack()
        self.entry_result = ctk.CTkEntry(self, state="readonly")
        self.entry_result.pack(pady=5)

        self.label_interest = ctk.CTkLabel(self, text="Total Interest Paid:")
        self.label_interest.pack()
        self.entry_interest = ctk.CTkEntry(self, state="readonly")
        self.entry_interest.pack(pady=5)

        # Nové pole pro celkovou částku k zaplacení
        self.label_total_payment = ctk.CTkLabel(self, text="Total Payment (Loan + Interest):")
        self.label_total_payment.pack()
        self.entry_total_payment = ctk.CTkEntry(self, state="readonly")
        self.entry_total_payment.pack(pady=5)

    def calculate(self):
        """ Funkce pro výpočet splátky, úroků a celkové částky """
        try:
            loan_amount = float(self.entry_amount.get().replace(" ", "").replace(",", "."))
            period = float(self.entry_period.get().replace(" ", "").replace(",", "."))
            rate = float(self.entry_rate.get().replace(" ", "").replace(",", "."))

            calculator = LoanCalculator(loan_amount, period, rate)
            monthly_payment = calculator.calculate_monthly_payment()
            total_interest = calculator.calculate_total_interest()
            total_payment = loan_amount + total_interest  # Celková částka k zaplacení

            # Formátování čísel s oddělovači tisíců
            formatted_payment = f"{monthly_payment:,.2f}".replace(",", " ").replace(".", ",")
            formatted_interest = f"{total_interest:,.2f}".replace(",", " ").replace(".", ",")
            formatted_total_payment = f"{total_payment:,.2f}".replace(",", " ").replace(".", ",")

            # Aktualizace výstupů
            self.entry_result.configure(state="normal")
            self.entry_result.delete(0, "end")
            self.entry_result.insert(0, f"{formatted_payment} Kč")
            self.entry_result.configure(state="readonly")

            self.entry_interest.configure(state="normal")
            self.entry_interest.delete(0, "end")
            self.entry_interest.insert(0, f"{formatted_interest} Kč")
            self.entry_interest.configure(state="readonly")

            self.entry_total_payment.configure(state="normal")
            self.entry_total_payment.delete(0, "end")
            self.entry_total_payment.insert(0, f"{formatted_total_payment} Kč")
            self.entry_total_payment.configure(state="readonly")

        except ValueError:
            self.entry_result.configure(state="normal")
            self.entry_result.delete(0, "end")
            self.entry_result.insert(0, "Invalid input")
            self.entry_result.configure(state="readonly")

            self.entry_interest.configure(state="normal")
            self.entry_interest.delete(0, "end")
            self.entry_interest.insert(0, "")
            self.entry_interest.configure(state="readonly")

            self.entry_total_payment.configure(state="normal")
            self.entry_total_payment.delete(0, "end")
            self.entry_total_payment.insert(0, "")
            self.entry_total_payment.configure(state="readonly")


# Spuštění aplikace
if __name__ == "__main__":
    app = LoanApp()
    app.mainloop()
