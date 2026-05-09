def main():
    # Získání zlomku od uživatele
    usr_fraction = input("Fraction: ").strip()

    # Volání funkce convert a uložení výsledku do proměnné
    result = convert(usr_fraction)

    # Zobrazení výsledku jako procenta nebo symbolu
    print(gauge(result))


def convert(fraction):
    """Konverze řetězce se zlomkem na hodnotu v rozmezí 0–100 (int)"""
    try:
        # Rozdělení řetězce na čitatel a jmenovatel
        x, y = fraction.split("/")
        x = int(x)  # Čitatel
        y = int(y)  # Jmenovatel

        # Kontrola dělení nulou
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        # Výpočet hodnoty zlomku jako procenta (int)
        fraction_value = (x / y) * 100

        # Kontrola, zda je hodnota zlomku mezi 0 a 100 %
        if fraction_value < 0 or fraction_value > 100:
            raise ValueError("Fraction must be between 0 and 1.")

        return int(fraction_value)  # Vrátíme hodnotu jako celé číslo

    except ValueError:
        raise ValueError("Please insert a valid fraction (e.g., '3/4').")


def gauge(percentage):
    """Vrátí procentuální hodnotu nebo symbol podle hodnoty zlomku"""
    # Porovnání hodnoty zlomku s hraničními hodnotami
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"  # Vrací procentuální hodnotu bez desetinných míst


if __name__ == "__main__":
    main()
