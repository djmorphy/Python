#Hogyan tudunk egy listának az elemein végig lépkedni és az összes lista elemmel
#valamilyen műveletet végrehajtani

gyumolcsok = ["alma", "körte", "cseresznye", "dinnye"]

#manualisan így csinálnám
# print(gyumolcsok[0])
# print(gyumolcsok[1])
# print(gyumolcsok[2])
# print(gyumolcsok[3])
# print(gyumolcsok[4])


# opció írunk egy for() ciklust ami arra alapul, hogy 0 index-el kezdődik és hogy lekérem a lenght-et 
# print(len(gyumolcsok)) és addig fog ismétlődni de pythonban van jobb 

# a for() ciklus azt mondja hogy létrehoz egy gyumolcs valtozot ami a gyumolcsok listan végig lépked 
# az elemeken akkor az adott elem a gyumolcs valtozóban lesz eltárolva és ezt a gyumlcs valtozot printeljuk ki

for gyumolcs in gyumolcsok:
    print(gyumolcs)

print()
print("következő feladat")


for betu in gyumolcsok[0]:
    print(betu)


print()
print("következő feladat amikor egybe ágyazom")

for gyumolcs in gyumolcsok:
    
    for betu in gyumolcs:
        print(betu)
    print()
