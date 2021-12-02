from random import randint

skupinaA = []
skupinaB = []
skupinaC = []
while True:
    meno = input("Zadaj meno:")
    if meno == "koniec":
        break
    randomSkupina = randint(0,2)
    if randomSkupina == 0:
        skupinaA.append(meno)
    elif randomSkupina == 1:
        skupinaB.append(meno)
    else:
        skupinaC.append(meno)
    print("V skupine A je: ", end = '')
    for i in skupinaA:
        print(i, ' ',end='')
    print("")
    print("V skupine B je: ", end='')
    for b in skupinaB:
        print(b, ' ', end='')
    print("")
    print("V skupine C je: ", end='')
    for c in skupinaC:
        print(c, ' ',end='')
    print("")
