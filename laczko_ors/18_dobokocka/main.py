import random
import time
# prjt lényege, hogy egy dobókocka app-ot fogunk írni ami random() számokat fog generálni
# a felhasználó kérésének megfelelően. A usernek lehetősége lesz megadni hány oldali
# dobókockával lehessen dobni és megkérdezzük hogy eldobjuk-e a kockát és ha igen
# akkor eldobjuk ha nem akkor kilépünk a programból. Ha invalid az input akkor szólunk


min_ertek = 1
max_ertek = 6

max_ertek_valasz=input("Hány oldalú legyen a dobókocka? (alapértelmezett = 6 )")

if max_ertek_valasz != "" and max_ertek_valasz.isnumeric():
    max_ertek = int(max_ertek_valasz)

def dobokocka_eldobasa():
    return random.randint(min_ertek, max_ertek)

def betoltes():
    print("Dobókocka eldobása:")
    time.sleep(0.5) #floadban adom meg a másodpercet.

while True:
    valasz = input("Eldobjuk a dobókockát?[i/n] ")

    if valasz == "i":
        betoltes()
        print(dobokocka_eldobasa())
    elif valasz == "n":
        print("Viszlát... ")
        break
    else:
        print("Invalid bevitel [i/n] ")
