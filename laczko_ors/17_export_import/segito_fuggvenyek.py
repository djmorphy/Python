#ki fogja írni milyen tranakciónk voltak. Zarojelben a tranzakciok listát várjuk mert a bankszamla.py -ben
# egy listával fogalmaztuk meg milyen tranzakciók voltak az elmult időben
#
#A tranzakcio listaba megkapjuk a koltekezéseket amit a tranzakcio list a tárol utána végig lépkedünk
# ezen a listán a tranzakcio valtozova és kinyomjuk a konzolra
def tranzakciok_megjelenitese(tranzakciok):
    for tranzakcio in tranzakciok:
        print(f"{tranzakcio}Ft értékű tranzakció")

#akkor szeretnénk a kiadások összegéhez hozzáadni azadott tranzakciót ha annak az értéke negativ összegű
def teljes_kiadas(tranzakciok):
    kiadasok_osszege = 0
    
    for tranzakcio in tranzakciok:
        if tranzakcio < 0:
            kiadasok_osszege += tranzakcio
    print(f"A teljes kiadások összege: {kiadasok_osszege} Ft ")


def teljes_bevetel(tranzakciok):
    bevetelek_osszege = 0

    for tranzakcio in tranzakciok:
        if tranzakcio > 0:
            bevetelek_osszege += tranzakcio
    print(f"A teljes bevételek összege: {bevetelek_osszege} Ft ")

