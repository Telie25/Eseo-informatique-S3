q_=int(input("Insérer le nombre décimal(base 10) à convertir:"))
q=q_
b=int(input("Insérer la base dans laquel convertir:"))
a=''
while q!=0:
    r=q%b
    a+=str(r)
    q=q//b
print(q_,"en base",b,"est",a[::-1])