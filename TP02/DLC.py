from colorama import Fore, Back, Style, init
init(autoreset=True)
import random
import copy
def print_table(table):
    col_widths = [
        max(len(str(row[i])) for row in table)
        for i in range(len(table[0]))
    ]
    for row in table:
        colored_cells = []
        for i, cell in enumerate(row):
            if cell == 2:
                color = Fore.RED
            elif cell == 1:
                color = Fore.BLUE
            else:
                color = Fore.WHITE
            colored_cells.append(
                color + str(cell).ljust(col_widths[i]) + Style.RESET_ALL
            )
        print(" | ".join(colored_cells))


def creation_grille():
    grille=[]
    for i in range (5):
        grille+=[[0,0,0,0,0]]
    a=b=c=d=0
    while a==c and a==d:
        a=random.randint(0,4)
        b=random.randint(0,4)
        c=random.randint(0,4)
        d=random.randint(0,4)
    grille[a][b]=1
    grille[c][d]=1
    return grille
def marquage(grille,a,b):
    if grille[a][b]==0:
        grille[a][b]=1
    elif grille[a][b]==1:
        grille[a][b]=0
def marquage_plus(grille,a,b):
    if a==0:
        if b==0:
            marquage(grille,a,b)
            marquage(grille,a+1,b)
            marquage(grille,a,b+1)
        elif b==4:
            marquage(grille,a,b)
            marquage(grille,a+1,b)
            marquage(grille,a,b-1)
        else:
            marquage(grille,a,b)
            marquage(grille,a+1,b)
            marquage(grille,a,b+1)
            marquage(grille,a,b-1)
    elif a==4:
        if b==0:
            marquage(grille,a,b)
            marquage(grille,a-1,b)
            marquage(grille,a,b+1)
        elif b==4:
            marquage(grille,a,b)
            marquage(grille,a-1,b)
            marquage(grille,a,b-1)
        else:
            marquage(grille,a,b)
            marquage(grille,a-1,b)
            marquage(grille,a,b+1)
            marquage(grille,a,b-1)
    else:
        if b==0:
            marquage(grille,a,b)
            marquage(grille,a+1,b)
            marquage(grille,a,b+1)
            marquage(grille,a-1,b)
        elif b==4:
            marquage(grille,a,b)
            marquage(grille,a-1,b)
            marquage(grille,a,b-1)
            marquage(grille,a+1,b)
        else:
            marquage(grille,a,b)
            marquage(grille,a+1,b)
            marquage(grille,a,b+1)
            marquage(grille,a,b-1)
            marquage(grille,a-1,b)        



def brulage(grille):
    for i in range(5):
        if grille[i][0]==1 or grille[i][0]==2:
            if grille[i][1]==1 or grille[i][1]==2:
                if grille[i][2]==1 or grille[i][2]==2:
                    if grille[i][3]==1 or grille[i][3]==2:
                        if grille[i][4]==1 or grille[i][4]==2:
                            for j in range (5):
                                grille[i][j]=2
        if grille[0][i]==1 or grille[0][i]==2:
            if grille[1][i]==1 or grille[1][i]==2:
                if grille[2][i]==1 or grille[2][i]==2:
                    if grille[3][i]==1 or grille[3][i]==2:
                        if grille[4][i]==1 or grille[4][i]==2:
                            for j in range (5):
                                grille[j][i]=2
    if grille[0][0]==1 or grille[0][0]==2:
            if grille[1][1]==1 or grille[1][1]==2:
                if grille[2][2]==1 or grille[2][2]==2:
                    if grille[3][3]==1 or grille[3][3]==2:
                        if grille[4][4]==1 or grille[4][4]==2:
                            for j in range (5):
                                grille[j][j]=2
    if grille[0][4]==1 or grille[0][4]==2:
            if grille[1][3]==1 or grille[1][3]==2:
                if grille[2][2]==1 or grille[2][2]==2:
                    if grille[3][1]==1 or grille[3][1]==2:
                        if grille[4][0]==1 or grille[4][0]==2:
                            for j in range (5):
                                grille[j][4-j]=2
def Bravo():
    print ('Bravo, vous avez réussi à entierement brûler la grille (bravo petit pyromane)')
    print('🔥\n🔥🔥\n🔥🔥🔥\n🔥🔥🔥🔥')
            



histo=[]
grille=creation_grille()
print_table(grille)
histo.append(copy.deepcopy(grille)) 
print(histo)
print('-----------------')
k=0

while k!='EXIT':
    k=input('Choisissez votre action: \n·xy pour marquer une case,\n·EXIT pour mettre fin à la partie,\n·UNDO pour revenir en arrière,\n·RESET pour recommencer la partie,\n·NEW pour commencer une nouvelle partie:')
    if k=='EXIT':
        break
    elif k=='CHEAT':
        grille=[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
        if grille==[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]:
            print_table(grille)
            histo.append(copy.deepcopy(grille))
            Bravo()
            break 
    elif k=='UNDO':
        histo.pop()
        grille=histo[-1]
        print_table(grille)
    elif k=='RESET':
        grille=histo[0]
        histo=[histo[0]]
        print_table(grille)
    elif k=='NEW':
        histo=[]
        grille=creation_grille()
        print_table(grille)
        histo.append(copy.deepcopy(grille))
    else:
        a=int(k[0])
        b=int(k[1])
        marquage_plus(grille,a,b)
        brulage(grille)
        print_table(grille)
        histo.append(copy.deepcopy(grille))
        if grille==[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]:
            Bravo()
            break

