baratok = ["Anna", "Péter", "Virág", "Viktor", "Klára", "Laci", "Ferenc"]

print(baratok[3])
print(baratok[0:3]) #az első három elemet kapom vissza. Addig fut le amíg a 3. -ba bele nem megy. Szóval az indexel vigyázni!
#2. elemtől a 4. elemig.  Péter indexe = 1 negyedik ember Viktor aminek index = 3 
print(baratok[1:4]) #outputja Péter Virág Viktor

#hány eleme van a listának
print(len(baratok))

#listának nem kell egy adattípusnak lennie
lista = ["szting", 10, 3.45]
print(lista)


#egyszer megadom az értékét onnantól kezdve nem változhatom. Nézd meg a tuples.py-t A zárójel típusa a fontos hogy mikor lehet
# változtatni és mikor nem  |==>tuples.py 
baratok = ["Kovács Anna", "Péter", "Virág", "Viktor", "Klára", "Laci", "Ferenc"]
baratok[0] = "Szűcs Anna"
print(baratok[0])


