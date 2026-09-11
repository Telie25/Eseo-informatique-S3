import random
L=[]
n=10
for i in range (n):
    L+=[random.randrange(0, 500)]
print(L)
a=True
for i in range(len(L)):
    b=L.pop(i)
    if b in L:
        a=False
        break
    L.insert(0,b)
print("Ils sont tous différents:",a)