#cél:  felhasznalotól bekérünk egy számot és annak a szorzótábláját végig írjuk. Pl input az 3. Akkor 1x3 = 3| 2x3 = 6 ...
#      és egy for() ciklus-al létrehozzuk




#mivel az input az szovegadat és soha nem konvertáltam int-é
#szorzando = input("Add meg a szorzandót: ")

#opció1
szorzando = int(input("Add meg a szozandót: "))

#opció2
# szorzando = input("Add meg a szozandót: ")




#designolás
print()
print(f"*     A {szorzando} szorzótábla    *")
print()

for szorzo in range(1, 11):

     print(f"{szorzo} * {szorzando} = {szorzo * szorzando}")
    
    #opció2 ha nem az input-ot konvertálom de inkább opció1 legyen.
    # print(f"{szorzo} * {szorzando} = {szorzo * int(szorzando)}")

