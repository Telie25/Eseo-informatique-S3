def ajout(filename, content):
    try:
        with open(filename, mode="a", encoding="utf-8") as file:
            file.write(content + "\n")
    except OSError as e:
        print(f"❌ Erreur lors de l'écriture dans le fichier : {e}")



def hanoi(n, source, target, auxiliary):
    if n == 1:
        ajout("hanoy.txt",f"Déplacer le disque 1 de {source} vers {target}")
    else:
        hanoi(n-1, source, auxiliary, target)
        ajout("hanoy.txt",f"Déplacer le disque {n} de {source} vers {target}")
        hanoi(n-1, auxiliary, target, source)
nombre_de_disques = 6
ajout("hanoy.txt",f"Solution pour {nombre_de_disques} disques:")
hanoi(nombre_de_disques, "A", "C", "B")