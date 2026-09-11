p=[10,2,'C','D','+']
pile=[]
for i in range (len(p)):
    if p[i]=='C':
        pile.pop(-1)
    elif p[i]=='D':
        pile.append(2*pile[-1])
    elif p[i]=='+':
        pile.append(pile[-2]+pile[-1])
    else:
        pile.append(p[i])
sum=0
for i in range(len(pile)):
    sum+=pile[i]
print("Le score final est de",sum)