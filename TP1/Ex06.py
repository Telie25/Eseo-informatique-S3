loop='o'
while loop=='o' or loop=='O':
    op=input("type d'opération souhaité: (a)ddition,(s)oustraction,(m)ultiplication ou (d)ivision:")
    if op!='a'and op!='s'and op!='m'and op!='d'and op!='A'and op!='S'and op!='M'and op!='D':
        print("calcul non-compris")
    else:
        a=float(input("Saisir un chiffre 1:"))
        b=float(input("Saisir un chiffre 2:"))
        if op=='a' or op=='A':
            result=a+b
            s='+'
        elif op=='s' or op=='S':
            result=a-b
            s='-'
        elif op=='m' or op=='M':
            result=a*b
            s='x'
        else:
            if b==0:
                result='division impossible'
            else:
                result=a/b
            s='÷'
        print("résultat:",a,s,b,'=',result)
    loop=input("un autre calcul? o/n")