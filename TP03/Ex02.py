def next_term(a):
    if a%2==0:
        return int(a/2)
    else:
        return a*3+1
def syraccus(s):
    s=next_term(s)
    print(s)
    if s!=1:
        syraccus(s)
    return
syraccus(5)