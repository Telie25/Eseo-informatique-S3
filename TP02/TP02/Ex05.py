from collections import deque
import copy
def deg_sup(d,a):
    return d.appendleft(a)
def poly():
    P=deque()
    deg=int(input('Insérer le degré du polynôme'))
    for i in range (deg+1):
        print('Insérer le facteur de degré',i)
        a=float(input())
        deg_sup(P,a)
    return P
def print_poly(Poly):
    P=copy.copy(Poly)
    answer=''
    l=len(P)
    for i in range (len(P)-2):
        answer+=str(P.popleft())
        answer+='x^'
        answer+=str(l-i-1)
        answer+='+'
    answer+=str(P.popleft())
    answer+='x'
    answer+='+'
    answer+=str(P.popleft())
    print(answer)
def destruc(P):
    for i in range (len(P)):
        P.pop()
    return P
def sum_poly(pa,pb):
    ps=deque()
    if len(pa)<=len(pb):
        pa,pb=pb,pa
    d=len(pa)-len(pb)
    for i in range(d):
        ps.append(pa.popleft())
    for i in range (d,len(pa)+d):
        ps.append(pa.popleft()+pb.popleft())
    return ps
def prod_poly(p,m):
    p_=copy.copy(p)
    m_=copy.copy(m)
    i=len(m_)
    a=0
    while a==0:
        a=m_.popleft()
        i-=1
    print(a,i)
    s=deque()
    for j in range (len(p_)):
        s.append(a*p_.popleft())
    for j in range (i):
        s.append(0)
    return s

