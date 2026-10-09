class AirPlane:
    def __init__(self,nom:str):
        self.nom=nom
        self.fly=False
    def TakeOff(self):
        self.fly=True
    def Land(self):
        self.fly=False
    def __str__(self):
        if self.fly:
            a='flying'
        else:
            a='ground'
        return (f"{self.nom} - {a}")
    
class MilitaryAircraft(AirPlane):
    def __init__ (self,nom:str,mission:str='no mission'):
        AirPlane.__init__(self,nom)
        self.mission=mission
    def __str__(self):
        return (f"{AirPlane.__str__(self)} - {self.mission}")
    def fini(self):
        self.mission='no mission'
class CargoAircraft(AirPlane):
    def __init__ (self,nom:str,shipment:str='no shipment'):
        AirPlane.__init__(self,nom)
        self.shipment=shipment
    def __str__(self):
        return (f"{AirPlane.__str__(self)} - {self.shipment}")  
    def vider(self):
        self.shipment='no shipment'
class CivilAircraft(AirPlane):
    def __init__ (self,nom:str,passengers:int=0):
        AirPlane.__init__(self,nom)
        self.passengers=passengers
    def __str__(self):
        return (f"{AirPlane.__str__(self)} - {self.passengers}")
    def vider(self):
        self.passengers=0
    def monter(self,number:int):
        self.passengers+=number

class Compagny():
    def __init__(self,nom:str='Compagnie'):
        self.nom=nom
        self.compo=[]
    def add(self,AirPlane):
        self.compo+=[AirPlane]
    def __str__(self):
        answer='['+self.nom+']\n'
        for i in range (len(self.compo)):
            answer+=str(self.compo[i])
            answer+='\n'
        return answer



com=Compagny('AirListembourg')
p1=CivilAircraft('Airbus A380')
p2=CargoAircraft('Airbus A300')
p3=MilitaryAircraft('Mig 21')
com.add(p1)
com.add(p2)
com.add(p3)
p1.monter(150)
p1.TakeOff()
p4=MilitaryAircraft('RTX5','Rescue Hostage')
p4.TakeOff()
com.add(p4)
print(str(com))



