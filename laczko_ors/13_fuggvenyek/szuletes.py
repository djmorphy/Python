idei_ev = 2023

felhasznalo1 = "Virág"
felhasznalo1_kor = 18
felhasznalo2 = "Emese"
felhasznalo2_kor = 20

#fgv nélkül egyenként így szívnék
# print(f"{felhasznalo1} {idei_ev - felhasznalo1_kor} -ban/ben született")

def mikor_szuletett(nev, kor):
    return f"{nev} {idei_ev - kor} -ban/ben született"

szoveg = mikor_szuletett("Péter", 42)
print(szoveg)

#ugyan az mintha a szöveget definiálom változóba és azt teszem be 14-15 sor kommenteléskor
print( mikor_szuletett("Péter", 42))
print(mikor_szuletett(felhasznalo1, felhasznalo1_kor,))
print(mikor_szuletett(felhasznalo2, felhasznalo2_kor))
#lehet "fél módon is" azaz egyiket váltózba adom meg a másikat meg explicit adom meg
print(mikor_szuletett(felhasznalo1, 19))


def udvozles(nev):
    print(f"Üdvözöllek{nev}!")