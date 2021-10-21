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