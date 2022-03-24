from random import randint
class Cube:
    def __init__(self, pocetStran):
        self.strany = pocetStran

    def hod_kockou(self, pocetHodov):

        for i in range(pocetHodov):
            cislo = randint(1, self.strany)
            print(str(cislo) + " ", end='')
        print("")

pocetStran = int(input("Zadaj počet strán prvej kocky: "))
kocka1 = Cube(pocetStran)
kocka1.hod_kockou(10)
pocetStran = int(input("Zadaj počet strán druhej kocky: "))
kocka2 = Cube(pocetStran)
kocka2.hod_kockou(10)