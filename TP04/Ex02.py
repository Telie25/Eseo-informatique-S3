class Fraction:
    def __init__(self,nume,deno):
        self.nume=nume
        self.deno=deno
    def __str__(self):
        return str(self.nume)+'/'+str(self.deno)
    def __add__(self,other):
        nume=self.nume*other.deno+other.nume*self.deno
        deno=self.deno*other.deno
        return nume,deno
    def __sub__(self,other):
        nume=self.nume*other.deno-other.nume*self.deno
        deno=self.deno*other.deno
        return nume,deno
    def __mul__(self,other):
        nume=self.nume*other.nume
        deno=self.deno*other.deno
        return nume,deno
    def __truediv__(self,other):
        nume=self.nume*other.deno
        deno=self.deno*other.nume
        return nume,deno
    def __gt__(self,other):
        return self.nume*other.deno>other.nume*self.deno
    def __lt__(self,other):
        return self.nume*other.deno<other.nume*self.deno    
    def __ge__(self,other):
        return self.nume*other.deno>=other.nume*self.deno
    def __le__(self,other):
        return self.nume*other.deno<=other.nume*self.deno 
    def __eq__(self,other):
        return self.nume*other.deno==other.nume*self.deno
    def __ne__(self,other):
        return self.nume*other.deno!=other.nume*self.deno 
    



a=Fraction(2,3)
b=Fraction(4,3)
print(str(a))
print(a+b,a-b,a*b,a/b,a>b,a<b,a==b,a!=b)