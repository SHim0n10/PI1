"""
    pole = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(pole[1][2])
    pole[0].append(99)

    for riadok in pole:
        for prvok in riadok:
            print(prvok)
"""
"""
def vypisKinosalu(kinosala):
    for riadok in kinosala:
        print(riadok)

kinosala = []
for i in range(5):
    temp = []
    for i in range(10):
        temp2 = []
        for i in range(4):
            temp2.append(0)
        temp.append(temp2)
    kinosala.append(temp)

kinosala[0][5] = 1
kinosala[2][4] = 1
kinosala[1][3] = 1
vypisKinosalu(kinosala)
"""
"""
niebielyRiadok = ["█"," ", "█"," ","█"," ","█"," "]
bielyRiadok = [" ", "█"," ","█"," ","█"," ","█"]
for i in range(4):
    for pismeno in niebielyRiadok:
        print(pismeno, end= "")
    print(sep= "")
    for j in bielyRiadok:
        print(j, end= "")
    print("")
"""

hracia_plocha = []
for i in range(3):
    temp = []
    for i in range(3):
        temp.append(0)
    hracia_plocha.append(temp)


hracia_plocha[1][2] = 1
hracia_plocha[0][1] = 2

for riadok in hracia_plocha:
    print(riadok)

#for kolo in range(10):
#    print(" ", end="")

for riadok1 in range(9):
    pokracovat = True

    poloha = []
    poziciay = int(input("Na aky riadok chces polozit?"))
    poziciax = int(input("Na aky stlpec chces polozit?"))
    poloha.append(poziciay)
    poloha.append(poziciax)
 #  print("poloha je", poloha)

    kontrola = hracia_plocha[poziciay][poziciax]
#   print(kontrola)
    if kontrola != 0:
        pokracovat = False
#    print(pokracovat)
    if pokracovat == True:
        counter = 1
        print(" ", end="")
        for i in range(3):
            print(i + 1, end="")
        print("")
        for riadok2 in hracia_plocha:
            print(counter, end="")
            counter = counter +1
            for pismenko in riadok2:
                if pismenko == 1:
                    print("x", end="")
                elif pismenko == 2:
                    print("o", end="")
                else:
                    print(" ",end="")
            print(" ")
        print("*******************************")


    pokracovat = True
    poziciay = int(input("Na aky riadok chces polozit?"))
    poziciax = int(input("Na aky stlpec chces polozite?"))
    poloha.append(poziciay)
    poloha.append(poziciax)
   # print("poloha je", poloha)
    if poziciay < 0:
        pokracovat = False
    elif poziciay > 2:
        pokracovat = False
    if poziciax < 0:
        pokracovat = False
    elif poziciax > 2:
        pokracovat = False
    if pokracovat == True:
        kontrola = hracia_plocha[poziciay][poziciax]
   # print(kontrola)
    if kontrola != 0:
        pokracovat = False
 #   print(pokracovat)
    if pokracovat == True:
        counter = 1
        print(" ", end="")
        for i in range(3):
            print(i + 1, end="")
        print("")
        for riadok2 in hracia_plocha:
            print(counter, end="")
            counter = counter + 1
            for pismenko in riadok2:
                if pismenko == 1:
                    print("x", end="")
                elif pismenko == 2:
                    print("o", end="")
                else:
                    print(" ", end="")
            print(" ")
        print("*******************************")
    elif pokracovat == False:
        print("neplatne cislo")
zoznam = []
zoznam.append(1)
print(zoznam)