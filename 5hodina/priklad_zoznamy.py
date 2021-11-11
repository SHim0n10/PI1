"""
zoznam_cisel = list(range(10,0, -1))
for i in zoznam_cisel:
    print(i)
print(zoznam_cisel)
pokracovanie = 'áno'
ovocie = ["jablko", "malina", "banán", "hruška",]
zelenina = ["paradajka", "uhorka", "kapusta", "brokolica"]
pocet_otazok = 0
while pokracovanie == 'áno':
    jedlo = input("Zadajte ovocie alebo zeleninu:")

    if jedlo in ovocie:
        print("Zadal si ovocie.")
    elif jedlo in zelenina:
        print("Zadal si zeleninu.")
    else:
        print("Tvoje slovo nemám v zozname")
    pocet_otazok = pocet_otazok + 1
    pokracovat = input("Chceš zadať ďalšie slovo? ")
    if pokracovat == 'nie':
        print("Spýtal si sa na", pocet_otazok, "otázok.")
        pokracovanie = 'nie'
"""
pokracovat = 1
zoznam_cisel = []
while pokracovat != '':
    vstup = input("Zadaj číslo:")
    pokracovat = vstup
    if vstup == '':
        break
    vstup = int(vstup)
    zoznam_cisel.append(vstup)

zoznam_cisel1 = sorted(zoznam_cisel)
dlzka_zoznamu = len(zoznam_cisel)
median_poradie = int(dlzka_zoznamu / 2)
median = zoznam_cisel1[median_poradie]
for i in range(dlzka_zoznamu):
    cislo = zoznam_cisel[i]
    cislo = int(cislo)
    rozdiel = cislo - median
    print(cislo, "sa od mediánu líši o", rozdiel)




