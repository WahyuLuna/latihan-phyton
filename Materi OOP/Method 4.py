class Hero():
    
    jumlah = 0
    
    def __init__(self, iname, ihealth,ipower,iarmor):
        self.name = iname
        self.health = ihealth
        self.power = ipower
        self.armor = iarmor
        Hero.jumlah += 1

        
    #Method function,tanpa argumen dan return
    def siapa(self):
        print(f"nama ku adalah : {self.name}")
        
    #Method dengan argumen, tanpa  return
    def healthup(self, up):
        self.health += up
        
    #Method dengan return
    def gethealth(self):
        return self.health


        
hero1 = Hero("Jhon",200,100,50)
hero2 = Hero("bob",150,200,50) 

print(hero1.__dict__)
hero1.siapa()
hero1.healthup(50)
print(hero1.health)
print(hero1.gethealth())

print(hero2.__dict__)
hero2.siapa()
hero2.healthup(50)
print(hero2.health)

print("Jumlah Charakter yang ada adalah = ",Hero.jumlah)