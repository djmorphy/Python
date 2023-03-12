#Mire jó a fgv?
#Ha van egy bizonyos feladat amit sokrszor el kell végezni akkor ne kelljen azt sokszor leírni vagy ha több adatot akarunk összefésülni
#és valamilyen müveletet végezni vele
idei_ev = 2023

felhasznalo1 = "Virág"
felhasznalo1_kor = 18
felhasznalo2 = "Emese"
felhasznalo2_kor = 20

#alapból ezt csinalnam
# print(f"Üdvözöllek {felhasznalo1}!")
# print(f"Üdvözöllek {felhasznalo2}!")



#alapból üdvözölné a rendszer és csak meg kéne adnom hogy milyen néven


#amikor meghívóom az üdvözlés fgv()-t abba lesz egy név és a név paraméter alapján ki fogja írni a program az üdvözlést
def udvozles(nev):
    print(f"Üdvözöllek {nev}!")


udvozles(felhasznalo1)
udvozles("Roli")
udvozles(felhasznalo2)

# |======> menj át a szuletes.py -be