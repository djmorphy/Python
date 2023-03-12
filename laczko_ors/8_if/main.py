# a = 10
# b = 20

#ha a és b egyenlő akkor történjen valami
#pythonba nem kötelező a zárójel és kettőspontot használunk a {} helyett
# if(a == b):
#     print("A és B egyenlő")

#valós használati ötlet
valasz = input("Kilépés a fiókból [igen/nem]? ")

if valasz == "igen":
    print("kilépés...")
elif valasz == "nem":
    print("nem léptél ki!")
elif valasz == "talán":
    print("talán maradok")
else:
    print("Érvénytelen válasz!")    