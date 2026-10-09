class Rectangle:
    def __init__(self,nom='rectangle',longueur=1,largeur=1):
        self.longueur=longueur
        self.largeur=largeur
        self.nom=nom
    def __str__(self):
        return (f"{self.nom},{self.longueur},{self.largeur}")
    
class Carre(Rectangle):
    def __init__(self,nom='carre',longueur=1):
        self.longueur=longueur
        self.largeur=longueur
        self.nom=nom

rec=Rectangle()
car=Carre()
print(str(rec),str(car))