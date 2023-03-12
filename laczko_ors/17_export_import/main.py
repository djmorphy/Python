#egy banki app lesz. Hogyan tudunk kódrészleteket importálni mert nem szerencsés egy file-ba tömöríteni mindent
#lesznek bankszámlák és ezeken a számlákon belül tudunk különböző műveleteket végrehajtani. Ki tudjuk számolni mennyi
# a bevétel mennyi a kiadás mennyi a trancakzió

#def osztály(tranzakcióklista, tulajdonos, egyenleg)


import bankszamla
import segito_fuggvenyek
#bankszamla egyszer azért mert a file-nak bankszamla a neve másodjára pedig azért mert az osztálynak
# is az a neve hogy bankszámla és utána példányosítom
feri_bankszamlaja = bankszamla.Bankszamla("Feri", 25000, [200000, -15000, -2000, 25000, -5000])

feri_bankszamlaja.szamlaadatok_kiirasa()


#A segito_fuggvenyek file-ból a tranzakciók_mejglenitese fgv-t szerenténk használni és
# paraméternek megadjuk feri_bankszamlaja -nak a tranzakcióit
segito_fuggvenyek.tranzakciok_megjelenitese(feri_bankszamlaja.tranzakciok)

#teljes kiadás
segito_fuggvenyek.teljes_kiadas(feri_bankszamlaja.tranzakciok)

#teljes bevétel
segito_fuggvenyek.teljes_bevetel(feri_bankszamlaja.tranzakciok)
