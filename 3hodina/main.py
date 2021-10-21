print("Aké je počiatočné číslo")
start = int(input())
print("Aké je koncové číslo")
koniec = int(input())

while (start <= koniec):
    if (start % 3 == 0):
        print(start)
    start = start + 1

