x=0
c=0
L=[]
while x==0:
    print("Insérer un nombre entiers")
    a=int(input())
    L+=[a]
    if a<=0:
        x=1
for i in range (len(L)):
    for j in range (0,len(L)-1):
        if L[j]>=L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
print("La liste triée est:",L)
print("Son minimum est:",L[0],"et son maximum est:",L[-1])
print("Sa valeur moyenne est:",sum(L)/len(L))

