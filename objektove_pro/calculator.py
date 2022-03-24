class Kalkulacka:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def scitanie(self):
        vysledok = self.number1 + self.number2
        return vysledok
    def odcitanie(self):
        vysledok = self.number1 - self.number2
        return vysledok
    def nasobenie(self):
        vysledok = self.number1 * self.number2
        return vysledok
    def delenie(self):
        vysledok = self.number1 / self.number2
        return vysledok
def matematika():
    cislo1 = int(input("Zadaj 1. číslo:"))
    cislo2 = int(input("Zadaj 2. číslo:"))



    pocitadlo = Kalkulacka(cislo1, cislo2)
    print("Súčet: " + str(pocitadlo.scitanie()))
    print("Rozdiel: " + str(pocitadlo.odcitanie()))
    print("Súčin: " + str(pocitadlo.nasobenie()))
    if cislo2 != 0:
        print("Podiel: " + str(pocitadlo.delenie()))
    matematika()

matematika()