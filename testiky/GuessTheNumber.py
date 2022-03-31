from random import randint

rekorder = ["", 0]
pocet_hier = 0
normalneCisla = False
pokracovat = True
kolo = 0
#priebeh hry
def hra():
    global kolo, pocet_hier
    kolo = 0
    name = getName()
    print("Vítam Ťa", name,end=''+ ".")
    print("")
    gameCount(pocet_hier)
    pocet_pokusov = getGuessCount()
    numberMinMax = getNumberMaxMin()
    randomHadaneCislo = randomGenerator(list(numberMinMax))
    vysledok = guessingNumber(pocet_pokusov, randomHadaneCislo)
    if vysledok[0] == "nie":
        print("Neuhádol si. Číslo bolo", randomHadaneCislo)
    if vysledok[0] == "áno":
        if int(rekorder[1]) == 0:
            print(name, "gratulujem, si nový rekordér s", vysledok[1], "pokusmi.")
            rekorder[0] = name
            rekorder[1] = vysledok[1]
            pocet_hier += 1
        elif int(rekorder[1]) > int(vysledok[1]):
            print(name, "gratulujem, si nový rekordér s", vysledok[1], "pokusmi.")
            rekorder[0] = name
            rekorder[1] = vysledok[1]
            pocet_hier += 1
        else:
            print("Prvý v tabuľke je ", rekorder[0], "s počtom pokusov", rekorder[1])
            pocet_hier += 1
    hrat_dalej = input("Ak chceš hrať ďalej napíš 'hra'.")
    if hrat_dalej == 'hra':
        hra()
        

#získa meno
def getName():
    meno = input("Ako sa voláš?>>>")
    return meno
#získa počet pokusov na uhádnutie
def getGuessCount():
    pocet_pokusov = input("Koľko by si chcel pokusov na uhádnutie čísla?>>>")
    return pocet_pokusov
#vypíše koľko bolo odohratých hier gramaticky správne
def gameCount(pocet_hier):
    if pocet_hier == 0:
        print("Zatiaľ nebola odohraná žiadna hra.")
    elif 4 >= pocet_hier > 1:
        print("Boli odohrané", pocet_hier, "hry.")
    else:
        print("Bolo odohraných", pocet_hier, "hier.")
#zistí a odkontroluje najmenšie a najväčšie možné hádané číslo
def getNumberMaxMin():
    global normalneCisla
    while normalneCisla != True:
        minimalneCislo = input("Aké má byť najmenšie hádané číslo?>>>")
        maximalneCislo = input("Aké má byť najväčšie hádané číslo?>>>")
        print(minimalneCislo, maximalneCislo)
        if int(maximalneCislo) < int(minimalneCislo):
            print("Prosím vlož čísla v správnom poradí")
        else:
            hadane_cislo = [minimalneCislo, maximalneCislo]
            normalneCisla = True
            return hadane_cislo
#vygeneruje random číslo
def randomGenerator(numberMinMax):
    minimalneCislo = int(numberMinMax[0])
    maximalneCislo = int(numberMinMax[1])
    randomCislo = randint(minimalneCislo, maximalneCislo)
    return randomCislo
#hádanie čísla
def guessingNumber(pocet_pokusov, hadane_cislo):
    global pokracovat, kolo
    pocet_pokusov = int(pocet_pokusov)
    i = 0
    while pokracovat:
        i += 1
        
        if i - 1 == pocet_pokusov:
            pokracovat = False
            return ["nie", 0]
            
        print(i, end=''+ ". pokus>>>")
        cislo = input("Hádaj číslo>>>")
        if int(cislo) == (hadane_cislo):
            kolo = i
            pokracovat = False
            print("Uhádol si!!!")
            return ["áno", kolo]
        else:
            if int(hadane_cislo) > int(cislo):
                print("Skús hádať vyššie.")
                kolo = i+1
            else:
                print("Skús hádať nižšie.")
                kolo = i+1
        

        

hra()