class Car:
    def __init__(self, znacka, rokVyroby, farba, sedadla, jeNastartovane):
        self.znacka = znacka
        self.rokVyroby = rokVyroby
        self.farba = farba
        self.sedadla = sedadla
        self.stav = jeNastartovane

    def chodDopredu(self):
        print("Auto ide dopredu.")
    def zatrub(self):
        print("tutuuuuuut")
    def nastartujVypni(self):
        if self.stav == 1:
            self.stav = 0
        elif self.stav == 0:
            self.stav = 1

    def __str__(self):
        print("Značka auta je " + self.znacka)
        print("Rok výroby auta je " + str(self.rokVyroby))
        print("Farba auta je " + self.farba)
        print("Počet sedadiel je " + str(self.sedadla))
        if self.stav == 1:
            print("Auto je naštartované.")
        else:
            print("Auto nie je naštartované.")


        print(self.stav)

        return " ";

auto = Car("BF458", 1857, "cervena", 5, 0)


auto.zatrub()
auto.chodDopredu()
print(auto)

auto.nastartujVypni()
print(auto)

