#kell egy összetevő lista
#kell egy öszetevő változ amivel chck hogy ki akar lépni vagy hozzáadni akar

osszetevok = []
#pythonban nem camelCase-t használunk hanem alulhuzasost
uj_osszetevo = ""

print("Összetevők megadása - kilépéshez használd a 'kilépés' szót")

while uj_osszetevo != "kilépés":
    uj_osszetevo = input("Adj meg egy összetevőt: ")

    #chck hogy nem entert nyom vagy nem azt írja hogy kilépés ami a recept része lenne
    if uj_osszetevo != "" and uj_osszetevo != "kilépés":
        osszetevok.append(uj_osszetevo)
        print(osszetevok)

print()
print("A  végső összetevők listája:")
print(osszetevok)   
