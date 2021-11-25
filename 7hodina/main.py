pocet_suborov = 60
vstup = []
basnicka = open("./basnicka.txt", encoding="utf-8")
for riadok in basnicka:
    vstup += riadok.split()
dlzka_basne = len(vstup)
k = dlzka_basne
j = 0
for i in range(pocet_suborov):

    if i >= k:
        j = i - dlzka_basne

    novy_subor = i
    filename = "%s.txt" % novy_subor
    otvoreny_subor = open(filename, mode="w", encoding="utf-8")
    print(vstup[j], file=otvoreny_subor)
    otvoreny_subor.close()
    j += 1
