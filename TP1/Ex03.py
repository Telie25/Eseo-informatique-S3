a_hum=float(input("Insérer le nombre d'année humaine à convertir:"))
if a_hum>=1:
    a_can=10.5+(a_hum-1)*4
    print(a_hum,"années humaine valle",a_can,"années canine")
elif a_hum>=0:
    a_can=10.5*a_hum
    print(a_hum,"année humaine valle",a_can,"année·s canine")
else:
    print("error, ce nombre d'année humaine n'est pas appropriée")