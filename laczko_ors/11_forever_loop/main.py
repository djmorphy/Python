#hasonlo mint a while de itt akkor lép ki ha beírom pl hogy k(kilépés) de addig fut
szam = 0

while True:
    print(f"A szám jelenlegi értéke: {szam}")
    bevitel = input("Mennyivel változtassuk a számot? [k = kilépés] ")
    if bevitel == "k": 
        break
    else:
        szam = szam + int(bevitel) 
    
    #na kezdődik bameg
    #ugyan azt jelenti
    szam += int(bevitel)

print(f"A szám végső értéke: {szam}")   