import random
def mots_du_fichier(nom_fichier):
    mots = []
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            mots_ligne = ligne.split()
            mots.extend(mots_ligne)
    return mots
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
def replace(mot,id,replacement):
    l=list(mot)
    l[id]=replacement
    return "".join(l)

def proposition(lettre,motc):
    global histo,mot,vies
    if lettre in histo:
        print('error: déjà-vu')
        print_mot(histo)
    elif lettre in mot:
        a=[pos for pos, char in enumerate(mot) if char == lettre]
        for i in range(len(a)):
            replace(mot,a[i],lettre)
        histo+=[lettre]
    else:
        vies-=1
        histo+=[lettre]




#système d'initialisation du jeu
dico = mots_du_fichier('dic.txt')
mot=random.choice(dico)
mot=mot.upper()
print(mot)
vies=7
cache=create_cache(mot)
print(cache)
histo=[]

#boucle de jeu
while vies!=0 or mot==mot_cache:
    prop=str(input('Insérer une proposition de lettre:'))
    if prop=='EXIT':
        vies=0
    proposition(prop,cache)
    print(cache)


print(vies,histo,cache)
