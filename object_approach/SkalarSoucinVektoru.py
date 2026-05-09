# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class MyVector:
    """PROGRAMEK PRO VYPOCET SKALARNIHO SOCINU VEKTORU A JINE FUNKCE"""

    # None - nastavi pocatecni hodnotu na NULL
    def __init__(self, vector=None):
        self.vector = vector

    def get_vector(self):
        return (self.vector)

    # Metoda vraci skalarni soucin vektoru
    def __mul__(self, other):
        sum = 0
        # v Cyklu mi len tolikrat pocita, kolik zjisti ze je prvku, vektoru
        # for cyklus i automaticky indexuje od 0
        for i in range(len(self.vector)):
            # self.vector je pripraven zde opet na nejcerstvejsi vstup
            # other.vector kopiruje hodnotu self.vector, nejcerstveji zadanou a drzi ji
            suma = sum + (self.vector[i] * other.vector[i])
        return suma

    # Metoda vraci soucet dvou vektoru, vysledek musi byt opet vektor
    def __add__(self, other):
        for j in range(len(other.vector)):
            # Vytvorena promenna add typu self
            self.add[j] = self.vector[j] + other.vector[j]
        return self.add[j]

    # Metoda vraci "Euklidovskou normu vektoru" tj. jeho delku, v podstate Pythagorovu vetu
    def norm(self):
        # 2 na 3ti se zapise 2**3, 2.odmocnina se zapise jako x**0.5#
        # Delka vektoru
        for k in range(len(other.vector)):
            self.u = (self.vector[j] ** 2) + (other.vector[j] ** 2)
        (self.u) ** 0.5
        return self.u