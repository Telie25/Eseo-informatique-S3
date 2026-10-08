import random
from colorama import Fore, Back, Style, init
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
            self.foreground_color='Black'
            self.background_color='White'
        elif i=='c':
            self.shade='♣'
            self.shade_name='Clover'
            self.foreground_color='Black'
            self.background_color='White'            
        elif i=='d':
            self.shade='♦'
            self.shade_name='Diamond'
            self.foreground_color='Red'
            self.background_color='Black'
        elif i=='h':
            self.shade='♥'
            self.shade_name='Heart'
            self.foreground_color='Red'
            self.background_color='Black'
        else:
            print('error002')
class Card:
    def __init__(self,pts,i):
        self.pts=pts
        self.i=i
    def __str__(self):
        return CardValue(self.pts).value_txt+CardColor(self.i).shade
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

def init52_cards():
    L=[]
    for j in range (1,14):
        for i in ('s','c','d','h'):
            L+=[Card(j,i)]
    return L
def Shuffle():
    return random.shuffle(deck)
def Draw():
    global hand
    hand+=[deck.pop(0)]
def Discard(card):
    global hand,defausse
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
        
#Card1=Card(3,'c')
#Card2=Card(4,'h')
#print(Card1<Card2)
deck=init52_cards()
hand=[]
defausse=[]
Shuffle()
score_user=0
score_com=0
Draw()
while score_user!=10 and score_com!=10:
    print_hand(hand)
    a=input("\nLa carte suivante sera supérieure (S), inférieure (I) ou égale (E)?:")
    if a=='I':
        Draw()
        if hand[-2]>hand[-1]:
            win()
        else:
            loose()
    elif a=='S':
        Draw()
        if hand[-2]<hand[-1]:
            win()
        else:
            loose()
    elif a=='E':
        Draw()
        if hand[-2]==hand[-1]:
            win()
        else:
            loose()
    elif a=='A':
        score_com=10
    else:
        print('error, commande non reconnue')
if score_user==10:
    print(f'Bravo, vous venez de gagner cette bataille à {10-score_com} point·s près, essayez de faire mieux la prochaine fois')
elif score_com==10:
    print (f"Malheuresement, vous venez de perdre face à l'ordinateur, à {10-score_user} point·s près vous auriez réussi, retentez votre chance")
