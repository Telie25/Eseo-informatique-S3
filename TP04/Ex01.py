class Product:
    def __init__(self,code,name,priceET,taxe=0.2):
        self.code=code
        self.name=name
        self.priceET=priceET
        self.taxe=taxe
    def get_price_it(self,priceET,taxe):
        return priceET*(1+taxe)

prod1=Product('aaa','Farine',1.0)
prod2=Product('aab','Lait',2.0)
print(f'{prod1.code}-{prod1.name}-{prod1.get_price_it(prod1.priceET,prod1.taxe)}')