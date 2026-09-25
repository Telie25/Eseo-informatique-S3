import random
import unicodedata
def mots_du_fichier(nom_fichier):
    mots = []
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            mots_ligne = ligne.split()
            mots.extend(mots_ligne)
    return mots
def replace(mot,id,replacement):
    global cache
    l=list(mot)
    l[id]=replacement
    cache="".join(l)
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
def print_mot(L):
    answer=''
    for i in range (len(L)):
        answer+=L[i]
    print(answer)
def create_cache(mot):
    answer=''
    answer+=mot[0]
    for i in range (len(mot)-1):
        answer+='_'
    return answer

def afficher_pendu(vies_restantes):
    etapes_pendu = [
        """
           ------
           |    |
           |    O
           |   /|\
           |   / \
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\
           |   / 
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |
        --------
        """
    ]
    vies_restantes = max(0, min(vies_restantes, 6))
    print(etapes_pendu[vies_restantes])

def proposition(lettre,motc):
    global histo,mot,vies,cache
    if lettre in histo:
        print('error: déjà-vu')
        print_mot(histo)
    elif lettre in mot:
        for i in range(len(mot)):
            if mot[i]==lettre:
                replace(cache,i,lettre)
        histo+=[lettre]
    else:
        vies-=1
        afficher_pendu(vies)
        histo+=[lettre]




#système d'initialisation du jeu
dico = mots_du_fichier('dic.txt')
mot=random.choice(dico)
mot=mot.upper()
mot=strip_accents(mot)
vies=7
cache=create_cache(mot)
print(cache)
histo=[]

#boucle de jeu
while vies!=0 and mot!=cache:
    prop=str(input('Insérer une proposition de lettre:'))
    print(prop)
    if prop=='EXIT':
        vies=0
        break
    proposition(prop,cache)
    print(cache)

if vies==0:
    print("T'es nul!")
else:
    print(f"Bravo, tu as réussi à trouver le mot:{mot} avec {vies} vies restantes")

