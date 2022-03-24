class Cat:
    # KONŠTRUKTOR -> Vykoná sa vždy keď VYTVÁRAM inštanciu triedy
    def __init__(self, name, vek):
        print("Vytvaram objekt mačky")
        self.name = name
        self.vek = vek

    def __str__(self):
        print("Meno mačky je: " + self.name)
        print("Vek mačky je: " + str(self.vek))
        return " ";

    def zamnaukaj(self):
        print(self.name + " mňau")

    def zjedz(self, jedlo):
        print(self.name + " zjedla/zjedlo " + jedlo)

#vytvorenie INŠTANCIE OBJEKTU mačka
cat = Cat("Mica", 4)

#volanie metody
cat.zamnaukaj()
cat.zjedz("rybu")

cat2 = Cat("Murko", 5)
cat.zamnaukaj()

print(cat2)
