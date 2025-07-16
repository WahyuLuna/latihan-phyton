class Hero(): #tempelate
    
    def __init__(self,inputname, inputpower,inputhealth, inputarmor):

        self.name = inputname
        self.power = inputpower
        self.health = inputhealth
        self.armor = inputarmor


hero1 = Hero("Jhon",200,100,50) #object
hero2 = Hero("bob",150,200,50) #object
hero3 = Hero("Ucup",200,1000,150) #object


# hero 1 atribute
print(hero1.__dict__)
print(hero1.name)
print(hero1.power)
print(hero1.health)
print(hero1.armor)

# hero 2 atribute
print(hero2.__dict__)
print(hero2.name)
print(hero2.power)
print(hero2.health)
print(hero2.armor)

# hero 3 atribute
print(hero3.__dict__)
print(hero3.name)
print(hero3.power)
print(hero3.health)
print(hero3.armor)

