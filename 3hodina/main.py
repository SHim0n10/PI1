"""
print("Aké je počiatočné číslo")
start = int(input())
print("Aké je koncové číslo")
koniec = int(input())

while (start <= koniec):
    if (start % 3 == 0):
        print(start)
    start = start + 1
"""

"""
samohlasky = "aeiouôáäéíúyý"
spoluhlasky = "qwrtzpsdfghjklxcvbnm"
cisla = "0123456789"


slovo = input("Zadaj slovo")

pocet_samohlasok = 0
pocet_spoluhlasky = 0
pocet_cisel = 0
pocet_znakov = 0

for znak in slovo:
    if znak in samohlasky:
        pocet_samohlasok = pocet_samohlasok + 1
    elif znak in spoluhlasky:
        pocet_spoluhlasky = pocet_spoluhlasky + 1
    elif znak in cisla:
        pocet_cisel = pocet_cisel + 1
    else:
        pocet_znakov = pocet_znakov + 1



print("Slovo obsahuje")
print(pocet_samohlasok, "samohlasok, ")
print(pocet_spoluhlasky, " spoluhlasok, ")
print(pocet_cisel, " cisel")
print( pocet_znakov, " znakov.")
"""
"""
zaciatok_prvy = int(input("Ako začína prvý interval"))
koniec_prvy = int(input("Ako končí prvý interval"))
zaciatok_druhy = int(input("Ako začína druhý interval"))
koniec_druhy = int(input("Ako končí druhý interval"))

koniec_druhy = koniec_druhy +1
koniec_prvy = koniec_prvy +1

for k in range(zaciatok_prvy, koniec_prvy):
    for l in range(zaciatok_druhy, koniec_druhy ):
        vysledok = k + l
        if vysledok in range(zaciatok_prvy,koniec_prvy):
            print("[",k,";", l,"]")
        elif vysledok in range(zaciatok_druhy, koniec_druhy):
            print("[", k, ";", l, "]")
"""
<<<<<<< HEAD
"""
riadky = int(input("Zadaj počet riadkov:"))
stlpce = int(input("Zadaj počet stlpcov:"))





for i in range(riadky):
    for p in range(stlpce):
        print("*", end= '')
    print( '',sep='')
"""
"""
vyska = int(input("Aka je vyska trojuholnika"))
strana = 1
for i in range(vyska):
    strana = strana + 2
for p in range(strana):
    medzera = p * 2
    medzera1 = medzera
    body = 1
    for k in range(vyska):

        while body <= strana:
            for j in range(medzera1):
                print('a', end= '')
            for b in range(body):
                print('*', end= '')
            print('',sep='')
            body = k + 2
            medzera1 = medzera1 - 2
"""
=======
znaky = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM&*;+ľščťžýáíé=´úäô§ň,.-12345678900%/("
for opak in range(slovo.len()):
    print(znaky[opak], end=, '')
    for opak2 in range(slovo.len()):
        print(znaky[opak2], end=, '')
        for opak3 in range(slovo.len()):
            print(znaky[opak3], end=, '')
            for opak4 in range(slovo.len()):
                print(znaky[opak4], end=, '')
                for opak5 in range(slovo.len()):
                    print(znaky[opak5], end=, '')
                    for opak6 in range(slovo.len()):
                        print(znaky[opak2], end=, '')
                        for opak7 in range(slovo.len()):
                            print(znaky[opak7], end=, '')
                            for opak8 in range(slovo.len()):
                                print(znaky[opak8], end=, '')
>>>>>>> 07a54dae9e1b0530a34dd4a227d3777ed786ec95
