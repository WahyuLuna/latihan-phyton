


class apple:
    color=""
    flafor=""
    size=""
    
fuji = apple()
fuji.color ="red"
fuji.flafor="sweet"
fuji.size ="small"

print(fuji.color,fuji.flafor,fuji.size)
    
american = apple()
american.color ="green"
american.flafor="soft"
american.size ="big"

print(american.color,american.flafor,american.size)

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class pig():
    name ="peppa"
    def speak(self):
        print(f"hai my name is {self.name}")
a = pig()        
a.speak()


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi my name is {}".format(self.name) 

# Create a new instance with a name of your choice
some_person = Person("asep")  
# Call the greeting method
print(some_person.greeting())


class Apple:
     def __init__(self, color, flavor):
         self.color = color
         self.flavor = flavor
     def __str__(self):
         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


jonagold = Apple("red", "sweet")
print(jonagold)


class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

class Animal:
     sound = ""
     def __init__(self, name):
         self.name = name
     def speak(self):
         print("{sound} I'm {name}! {sound}".format(
             name=self.name, sound=self.sound))
 
class Piglet(Animal):
     sound = "Oink!"
 
class Cow(Animal):
     sound = "Moooo"


hamlet = Piglet("Hamlet")
print(hamlet.speak())
 
class Cow(Animal):
     sound = "Moooo"
 
milky = Cow("Milky White")
milky.speak()

class Repository:
      def __init__(self):
          self.packages = {}
      def add_package(self, package):
          self.packages[package.name] = package
      def total_size(self):
          result = 0
          for package in self.packages.values():
              result += package.size
          return result




