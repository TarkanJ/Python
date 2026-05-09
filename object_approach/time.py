"""
VSTUP A VYSTUP (I/O) - JAK BY MEL VYPADAT!!!

cas1 = MyTime([1,20])    # Zadal jsem 2 parametry - 1 hodina a 20 minut
MyTime.get_mins(cas1)    # Zavolam tzv. "modul" tak se rika v Pythonu take funkci
80                       # Tento modul/funkce mi vratila cas v minutach
MyTime.mins_to_time(80)  # Kdyz opet zavolam modul, s prechozi hodnotou
[1, 20]                  # ... modul mi vrati vypocet pro puvodne zadany cas!!!
"""

class MyTime:
    # Parametr time je volitelný /mutable/ a má výchozí hodnotu [0, 0],
    # což znamená, že pokud není předána žádná hodnota, bude čas nastaven na 0 hodin a 0 minut
    def __init__(self, time=[0, 0]):
        self.time = time

    def get_mins(self):
        # self.time[0] * 60 převede hodiny na minuty
        # self.time[1] přičte minuty
        return (self.time[0] * 60 + self.time[1])

    def mins_to_time(mins):
        # mins // 60 vypočítá celé hodiny
        # mins % 60 vypočítá zbývající minuty
        return ([mins // 60, mins % 60])

    def __str__(self):
        return f"{self.time}"


def main():
    # Pokud zadáme čas ve formátu [hodina, minuta] bude zobrazen výsledný počet minut
    cas1 = MyTime([1, 20])
    print(MyTime.get_mins(cas1))

    # Pokud zde zadáme počet minut, výsledek se zobrazí jako [celé hodiny, celé minuty]
    print(MyTime.mins_to_time(180))
    cas2 = MyTime.get_mins(cas1)
    print(MyTime.mins_to_time(cas2))

"""
    casik = get_time()
    print(MyTime.mins_to_time(casik))

def get_time():
    minutky = input("Zadej minuty: ")
    # hodiny_minuty = input("Zadej hodiny a minuty: ")
    return MyTime(minutky)
"""

if __name__ == "__main__":
    main()