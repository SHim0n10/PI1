def jePalindrom(slovo):
    priklad = ''
    for i in slovo:
        priklad = i + priklad
    if priklad == slovo:
        print("Je to palindrom")
    else:
        print("nie je to palindrom")

jePalindrom("oko")

#otacanie : otocene_slovo = slovo[::-1]