

import sys

# Vérification des arguments passés en ligne de commande
def main():
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: ./HeadTail.py head/tail nombre chemin_fichier")

        mode = sys.argv[1].lower()
        n_lignes = sys.argv[2]
        chemin_fichier = sys.argv[3]

        # Vérification du premier paramètre : head ou tail
        if mode not in ["head", "tail"]:
            raise ValueError("Le premier paramètre doit être 'head' ou 'tail'")

        # Vérification du second paramètre : entier positif
        if not n_lignes.isdigit() or int(n_lignes) <= 0:
            raise ValueError("Le deuxième paramètre doit être un entier positif")
        n_lignes = int(n_lignes)

        # Lecture du fichier
        try:
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                lignes = f.readlines()
        except FileNotFoundError:
            raise IOError(f"Fichier introuvable : {chemin_fichier}")

        # Affichage selon head ou tail
        if mode == "head":
            for ligne in lignes[:n_lignes]:
                print(ligne.rstrip())
        else:  # tail
            for ligne in lignes[-n_lignes:]:
                print(ligne.rstrip())

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
    except IOError as ioe:
        print(f"Erreur d'entrée/sortie : {ioe}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()