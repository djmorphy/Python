#szükségem lesz 3 változóra amiben el tudom menteni az datokat
#kell egy input rész ahova a user beírja a dolgait
#ki kell cserélnem az értékeket a bevitt értékekre
#a beírt inputot össze kell füzzem a print-ben lévő static szöveggel

"""
szin = "piros"
fonev = "füzet"
melleknev = "szép"

#Template literal string
print(f"A rózsa  {szin}")
print(f"A {fonev} pedig kék ")
print(f"Eddig nagyon {melleknev} az év")

"""

szin = input("Egy szín: ")
fonev = input("Egy főnév: ")
melleknev = input("Egy melléknév: ")

print()
print(f"A rózsa  {szin}")
print(f"A {fonev} pedig kék ")
print(f"Eddig nagyon {melleknev} az év")