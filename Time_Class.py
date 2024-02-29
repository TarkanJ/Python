""" TROCHU OSVETLENI S TRIDY A OBJEKTY A PROMENNOU "self" """
class MyTime:
    "self ukazuje na nase vlastni data"
    def __init__(self, time=[0,0]):
        self.time = time
        
    def get_mins(self):
        return(self.time[0]*60+self.time[1])
            
    def mins_to_time(mins):
        return([mins//60,mins%60])

"""
VSTUP A VYSTUP (I/O) - JAK BY MEL VYPADAT!!!

cas1 = MyTime([1,20])    # Zadal jsem 2 parametry - 1 hodina a 20 minut
MyTime.get_mins(cas1)    # Zavolam tzv. "modul" tak se rika v Pythonu take funkci
80                       # Tento modul/funkce mi vratila cas v minutach
MyTime.mins_to_time(80)  # Kdyz opet zavolam modul, s prechozi hodnotou
[1, 20]                  # ... modul mi vrati vypocet pro puvodne zadany cas!!!
"""