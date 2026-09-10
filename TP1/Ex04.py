n=int(input("Insérer le nombre d'approximation à obtenir:"))
if n>=0:
    pi=3
    for i in range (1,n+1):
        if i%2==1:
            pi+=4/((2*i)*(2*i+1)*(2*i+2))
            print("La",i,"ième approximation est:",pi)
        else:
            pi-=4/((2*i)*(2*i+1)*(2*i+2))
            print("La",i,"ième approximation est:",pi)
else:
    print("error, ce nombre d'approximation n'est pas approprié")