class LoanCalculator:
    def __init__(self, loan_amount, period_in_years, rate):
        """
        Inicializace objektu LoanCalculator.
        :param loan_amount: Výše úvěru
        :param period_in_years: Doba splácení v letech
        :param rate: Úroková sazba v procentech
        """
        self.loan_amount = loan_amount
        self.period_in_years = period_in_years
        self.rate = rate / 100  # Převod sazby na desetinnou hodnotu

    def years_to_months(self):
        """ Převádí roky na měsíce. """
        return self.period_in_years * 12

    def monthly_rate(self):
        """ Výpočet měsíční úrokové sazby. """
        return self.rate / 12

    def calculate_monthly_payment(self):
        """
        Výpočet měsíční splátky na základě anuity.
        Formula: S = U × [qn × (q − 1) / (qn − 1)]
        """
        q = 1 + self.monthly_rate()
        n = self.years_to_months()
        qn = float(pow(q, n))
        calcul = qn * (q - 1)
        return self.loan_amount * (calcul / (qn - 1))

    def calculate_total_interest(self):
        """
        Výpočet celkové částky zaplacené na úrocích.
        """
        total_monthly_payment = self.calculate_monthly_payment() * self.years_to_months()
        total_interest = total_monthly_payment - self.loan_amount
        return total_interest
