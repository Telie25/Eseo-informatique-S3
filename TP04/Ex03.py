import random
from colorama import init
from termcolor import colored

init(autoreset=True)
class CardValue:
    def __init__(self,pts):
        self.value_pts=pts
        if pts<=10 and pts>=1:
            self.value_txt=str(pts)
        elif pts==11:
            self.value_txt='J'
        elif pts==12:
            self.value_txt='Q'
        elif pts==13:
            self.value_txt='K'
        else:
            print('error001')
class CardColor:
    def __init__(self,i):
        if i=='s':
            self.shade='♠'
            self.shade_name='Spear'
            self.foreground_color='black'
            self.background_color='white'
        elif i=='c':
            self.shade='♣'
            self.shade_name='Clover'
            self.foreground_color='black'
            self.background_color='white'            
        elif i=='d':
            self.shade='♦'
            self.shade_name='Diamond'
            self.foreground_color='red'
            self.background_color='white'
        elif i=='h':
            self.shade='♥'
            self.shade_name='Heart'
            self.foreground_color='red'
            self.background_color='white'
        else:
            print('error002')
class Card:
    def __init__(self,pts,i):
        self.pts=pts
        self.i=i
    def __str__(self):
        return colored(CardValue(self.pts).value_txt+CardColor(self.i).shade,CardColor(self.i).foreground_color,'on_'+CardColor(self.i).background_color)
    def __repr__(self):
        return CardValue(self.pts).value_txt+CardColor(self.i).shade_name 
    def __eq__(self,other):
        return self.pts==other.pts
    def __gt__(self,other):
        return self.pts>other.pts
    def __lt__(self,other):
        return self.pts<other.pts


def print_hand(hand):
    print(end='|')
    for i in range(len(hand)):
        print(str(hand[i]), end='|')

class Deck:
    def __init__(self):
        self.deck=[]
        for j in range (1,14):
            for i in ('s','c','d','h'):
                self.deck+=[Card(j,i)]
        random.shuffle(self.deck)
    def Draw(self,hand):
        hand+=[self.deck.pop(0)]
    def Discard(self,card,hand):
        global defausse
        if card in hand:
            hand.remove(card)
            defausse+=[card]


def win():
    global score_user,score_com
    score_user+=1
    print(f"Bravo, vous venez de marquer un point,{score_user}-{score_com}")
def loose():
    global score_user,score_com
    score_com+=1
    print(f"Loupé, l'ordinateur marque un point,{score_user}-{score_com}")
        
#Initialisation
deck=Deck()
hand=[]
defausse=[]

score_user=0
score_com=0
deck.Draw(hand)

#Boucle de jeu
while score_user!=10 and score_com!=10:
    print_hand(hand)
    a=input("\nVous souhaitez: abandonner (A), Voir l'historique (H)\nVous pensez que la carte suivante sera: supérieure (S), inférieure (I) ou égale (E)?:")
    if a=='I':
        deck.Draw(hand)
        if hand[-2]>hand[-1]:
            win()
        else:
            loose()
        deck.Discard(hand[0],hand)
    elif a=='S':
        deck.Draw(hand)
        if hand[-2]<hand[-1]:
            win()
        else:
            loose()
        deck.Discard(hand[0],hand)
    elif a=='E':
        deck.Draw(hand)
        if hand[-2]==hand[-1]:
            win()
        else:
            loose()
        deck.Discard(hand[0],hand)
    elif a=='A':
        score_com=10
    elif a=='H':
        print('La défausse est composée de:',end='')
        print_hand(defausse)
        print(end='\n')
    else:
        print('error, commande non reconnue')

#Résultat
if score_user==10:
    print(f'Bravo, vous venez de gagner cette bataille à {10-score_com} point·s près, essayez de faire encore mieux la prochaine fois!')
elif score_com==10:
    print (f"Malheuresement, vous venez de perdre face à l'ordinateur, à {10-score_user} point·s près vous auriez réussi, retentez votre chance!")
