class Hero(): #tempelate
    
    #Class variable 
    jumlah = 0
    
    def __init__(self,inputname, inputpower,inputhealth, inputarmor):
        # intance variable (variable yan hanya akan dimiliki oleh hero sj)
        self.name = inputname
        self.power = inputpower
        self.health = inputhealth
        self.armor = inputarmor
        Hero.jumlah += 1


hero1 = Hero("Jhon",200,100,50) #object
hero2 = Hero("bob",150,200,50) #object
hero3 = Hero("Ucup",200,1000,150) #object


print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print("Jumlah Charakter yang ada adalah = ",Hero.jumlah)