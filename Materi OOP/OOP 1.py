class Hero(): #tempelate
    pass


hero1 = Hero() #object
hero2 = Hero() #object
boss = Hero() #object

hero1.name = "John"
hero1.health = 100

hero2.name = "Bob"
hero2.health = 100

boss.name = "Ucup"
boss.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)
print(hero1.health)


