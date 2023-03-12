#kód addig fut amíg valami be nem teljesül. PL.: a számokat tudjuk össze adni amíg el nem érjük a 100-at. És a usertől függ hogy milyen
# számokat ad hozzá

szam = 0


while szam < 100:
    print(f"A szám értéke: {szam}")
    szam = szam + int(input("Mennyivel növeljük a számot? "))

print(f"A szám végső értéke {szam}")
    