filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = []
for name in filenames:

    if name.endswith("hpp"):
        new = name.replace("hpp","p")
        newfilenames.append(new)

    else:
        newfilenames.append(name)  
            
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = ___
#   for word in words:
#     # Create the pig latin word and add it to the list
#     ___
#     # Turn the list back into a phrase
#   return ___
		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def group_list(group, users):
  members = users
  return group + ": " + ", ".join(members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

def guest_list(guests):
	for name,age,job in guests:
	
		print("{} is {} years old and work as {}".format(name,age,job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

