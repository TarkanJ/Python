from tkinter import *

""" Program načte textový soubor a po kliknutí ho zobrazí """

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Martino FB Kontakty:")
        self.pack(fill=BOTH, expand=1)

        # Tlačítko pro generování kódu
        codeButton = Button(
            self,
            text="Zobraz",
            command=self.generatecode
        )
        codeButton.place(x=10, y=10)

        # Textové pole pro zobrazení obsahu souboru
        global t
        t = Text(self, wrap=WORD, width=48, height=15)
        t.place(x=10, y=50)

    def generatecode(self):
        pocetZaznamu = 0
        try:
            # Otevře soubor pro čtení
            # with open("codes.txt", "r") as f:
            with open("kontakty_rijen2025.txt", "r", encoding="utf-8") as f:
                content = f.read()
                pocetZaznamu += 1

            # Vloží obsah do textového pole
            t.delete(1.0, END)  # Vymaže stávající obsah
            t.insert(END, content)
            t.insert(END, pocetZaznamu)
        except FileNotFoundError:
            t.delete(1.0, END)
            t.insert(END, "Soubor nebyl nalezen.")


# Inicializace hlavního okna
root = Tk()
root.geometry("400x300")  # Nastavení velikosti okna
app = Window(root)
root.mainloop()
