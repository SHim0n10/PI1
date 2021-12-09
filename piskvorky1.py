hracia_plocha = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]
h = []
h = hracia_plocha
k1 = 0
k2 = 0
k3 = 0
h1 = hracia_plocha
def nakresli(hracia_plocha):
    print("  ",end="")
    for k in range(3):
        print("|", k +1,"",end="")


    print("|")

    counter = 1
    print("---------------")

    for riadok in hracia_plocha:

        print(counter,"|", end="")
        counter = counter + 1

        for j in riadok:
            if j == 0:
                print("   |", end="")
            elif j == 1:
                print(" x |", end="")
            else:
                print(" o |",end="")
        print("")
        print("---------------")
def kontrolavyhry(h):

        
        #kontrola_diagonalne1
        k1 = h[0][0]
        k2 = h[1][1]
        k3 = h[2][2]
        if k1 == k2:
            if k2 == k3:
                return k1
        #kontrola_diagonalne2
        k1 = h[0][2]
        k2 = h[1][1]
        k3 = h[2][0]
        if k1 == k2:
            if k2 == k3:
                return k1
        #kontrola_vertikalne1
        k1 = h[0][0]
        k2 = h[0][1]
        k3 = h[0][2]
        if k1 == k2:
            if k2 == k3:
                return k1
        #kontrola_vertikalne2
        k1 = h[1][0]
        k2 = h[1][1]
        k3 = h[1][2]
        if k1 == k2:
            if k2 == k3:
                return k1
        #kontrola_vertikalne3
        k1 = h[2][0]
        k2 = h[2][1]
        k3 = h[2][2]
        if k1 == k2:
            if k2 == k3:
                return k1
        #kontrola_horizontalne1
        k1 = h[0][0]
        k2 = h[1][0]
        k3 = h[2][0]
        if k1 == k2:
            if k2 == k3:
                return k1
        #kontrola_horizontalne2
        k1 = h[0][1]
        k2 = h[1][1]
        k3 = h[2][1]
        if k1 == k2:
            if k2 == k3:
                return k1
        #kontrola_horizontalne1
        k1 = h[0][2]
        k2 = h[1][2]
        k3 = h[2][2]
        if k1 == k2:
            if k2 == k3:
                return k1
def volne_miesto(pozicia):
    if pozicia == 1:
        kontrola = h[0][0]
    if pozicia == 2:
        kontrola = h[0][1]
    if pozicia == 3:
        kontrola = h[0][2]
    if pozicia == 4:
        kontrola = h[1][0]
    if pozicia == 5:
        kontrola = h[1][1]
    if pozicia == 6:
        kontrola = h[1][2]
    if pozicia == 7:
        kontrola = h[2][0]
    if pozicia == 8:
        kontrola = h[2][1]
    if pozicia == 9:
        kontrola = h[2][2]
    if pozicia > 9:
        kontrola = 1
    if pozicia < 1:
        kontrola = 1
    
    if kontrola == 0:
        return True
    else:
        return False
def vymen_hracov(pozicia, hrac):
    
    if pozicia == 1:
        h1[0][0] = hrac
    if pozicia == 2:
        h1[0][1] = hrac
    if pozicia == 3:
        h1[0][2] = hrac
    if pozicia == 4:
        h1[1][0] = hrac
    if pozicia == 5:
        h1[1][1] = hrac
    if pozicia == 6:
        h1[1][2] = hrac
    if pozicia == 7:
        h1[2][0] = hrac
    if pozicia == 8:
        h1[2][1] = hrac
    if pozicia == 9:
        h1[2][2] = hrac
    return h1
#Zmena plochy: h1 = vymen_hracov(pozicia, cislo_hraca)
pokracovat = 0
counter_hraca = 1
counter_kolo = 1
while pokracovat == 0:
    print(nakresli(h1))
    hrac_na_rade = counter_hraca % 2
    mozne_hrat1 = False
    mozne_hrat2 = False

    if hrac_na_rade == 1:
        print("Hrac 1 s X je na rade:")
        while mozne_hrat1 == False:
            
            pozicia = int(input("Napíš pozíciu od 1 do 9 =>"))
            if volne_miesto(pozicia) == False:
                mozne_hrat1 = False
                print("Zadal si nesprávne alebo už obsadené číslo.")
            else:

                mozne_hrat1 = True
        h1 = vymen_hracov(pozicia, 1)

    elif hrac_na_rade == 0:
        print("Hrac 2 s O je na rade:")
        while mozne_hrat2 == False:
            
            pozicia = int(input("Napíš pozíciu od 1 do 9 =>"))
            if volne_miesto(pozicia) == False:
                mozne_hrat2 = False
                print("Zadal si nesprávne alebo už obsadené číslo.")
            else:
                
                mozne_hrat2 = True
        h1 = vymen_hracov(pozicia, 2)
    
    print(nakresli(h1))
    vyhra = kontrolavyhry(h1)
    if vyhra == 1:
        print("Hráč 1 vyhral s X-kami")
        break
    elif vyhra == 2:
        print("Hráč 2 vyhral s O-čkami")
        break

    counter_hraca = counter_hraca + 1
    counter_kolo = counter_kolo + 1
    if counter_kolo == 10:
        print("Je to remíza.")
        break

