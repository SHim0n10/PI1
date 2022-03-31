
for i in range(100):
    i += 1
    if i % 2 == 1:
        print("Hrac_1 >>>", end='')
    else:
        print("Hrac_2 >>>", end='')
    if i % 3 == 0:
        if i % 5 == 0:
            print("HalaBala")
        else:
            print("Hala")
    elif i % 5 == 0:
        print("Bala")
    else:
        print(i)