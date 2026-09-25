import random
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
def uniformiser(mo):
    global mot,cache
    if '-' in mo:
        for i in range(len(mo)):
            if mo[i]=='-':
                replace(cache,i,'-')
    if 'É' in mo:
        for i in range(len(mot)):
            if mo[i]=='É':
                replace(cache,i,'E')
                replace(mot,i,'E')
    if 'È' in mo:
        for i in range(len(mot)):
            if mo[i]=='È':
                replace(cache,i,'E')
                replace(mot,i,'E')
    if 'Ê' in mo:
        for i in range(len(mot)):
            if mo[i]=='Ê':
                replace(cache,i,'E')
                replace(mot,i,'E')
    if 'À' in mo:
        for i in range(len(mot)):
            if mo[i]=='À':
                replace(cache,i,'A')
                replace(mot,i,'A')
    if 'Ç' in mo:
        for i in range(len(mot)):
            if mo[i]=='Ç':
                replace(cache,i,'C')
                replace(mot,i,'C')
    if 'Ù' in mo:
        for i in range(len(mot)):
            if mo[i]=='Ù':
                replace(cache,i,'U')
                replace(mot,i,'U')


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
uniformiser(mot)
print(mot)
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
    print("Bravo, tu as réussi à trouver le mot:",mot,"avec",vies,"vies restantes")

