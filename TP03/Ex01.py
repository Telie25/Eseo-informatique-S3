import copy
def fac(n,r):
    if n!=1:
        r*=n
        n-=1
        fac(n,r)
    else:
        return r
print(fac(5,1))

