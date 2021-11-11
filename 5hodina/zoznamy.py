zoznam_prazdny = []
zoznam_cisel = [1,5,8,9,40,21]
zoznam_pismen = ['a','b']
zoznam_mix = ["slovo", 14, 'a', 55]

zoznam_cisel[0] = 9999
print(zoznam_cisel[4])
print(zoznam_pismen[1])
print(zoznam_mix[-1])

print(zoznam_cisel)
print(zoznam_pismen)
print(zoznam_mix)
print("------------")

zoznam = list()
print(zoznam)
zoznam_range = list(range(3, 7))
print(zoznam_range)

print("-------")

#NEOREZANY zoznam
neorezany_zoznam = list(range(10))
print(neorezany_zoznam)

print(neorezany_zoznam[0:5])
print(neorezany_zoznam[2:8])
print(neorezany_zoznam[1:7:2])
print(neorezany_zoznam[2:9:3])

#Velkost zoznamu
x = [5,8,1,3,"slovo"]
print(len(x))

#PRechádzanie zoznamu
zoznam_prvkov = ["jablko", "hruška", "banán"]
#1.
for prvok in zoznam_prvkov:
    print(prvok)
#2.
for index in range(len(zoznam_prvkov)):
    print(zoznam_prvkov[index])

print("-------")

#Metódy pre zoznamy
myList = [1,5,55,500]
#append
myList.append(99)
print(myList)
#pop
hodnota = myList.pop()
print(myList)
print(hodnota)

#Funkcie pre zoznamy
#len
#min/max
#sum
#sorted
myList2 = [1,54,7,2,74,-128]
print("minimum",min(myList2))
print("maximum",max(myList2))
print("sumár", sum(myList2))

print(myList2)
print(sorted(myList2))
