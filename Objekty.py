""" ZAKLADNI VZTAHY MEZI OBJEKTY a "self" "other" """
class Pocty:
    def __init__(self,other=None):
        self.a = 2
        self.b = 5
        # a.self = 2
        # b.other = 5
    
    "Funkce, co secte dve cisla"
    def secti(self): # definice prvni metody
        return print(self.a + self.b)
    
    "Funkce, co odecte dve cisla"
    def odecti(self): # definice prvni metody
        return print(self.a - self.b)
    
"""
PREDPOKLADANY VSTUP
-------------------
novyObjekt = Pocty()
novyObjekt.secti()
7
novyObjekt.odecti()
-3
"""