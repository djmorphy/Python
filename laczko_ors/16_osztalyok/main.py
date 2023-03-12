#bizonyos adatokat szeretnék egyszerre tárolni
#embereket tartunk számot pl egy chat app-ban. Egy emberhez tartozik több adat is pl név kor hobbi stb
#a chatet is obj-ként is tárolhatjuk mert ki küldte mikor küldte mi a tartalma

class Ember:
    #az osztálynak kell mindig egy __init__ -je
    def __init__(self, nev, kor, lakhely):
        self.nev = nev
        self.kor = kor
        self.lakhely = lakhely

    def bemutatkozas(self):
        print(f"Én vagyok {self.nev}, {self.kor} éves vagyok, {self.lakhely} -ról/ről.")



#ebbe a felhasznalo1 elmentettünk egy obj aminek két paramétere van amit az init fgv-ben rendeltük hozzá
# ehhez az ember obj-hez
felhasznalo1 = Ember("Ferenc", 20, "Budapest")
felhasznalo2 = Ember("Viki", 25, "Gyula")
felhasznalo3 = Ember("Roli", 34, "Mkháza")

print(felhasznalo1.nev)
print(felhasznalo3.lakhely)

felhasznalo1.bemutatkozas()
felhasznalo2.bemutatkozas()
felhasznalo3.bemutatkozas()
