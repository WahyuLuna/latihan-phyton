x = ["now", "we", "are", "cooking !"]
print(type(x))
print(x)
len(x)
print("are"in x)
print(x[0])
print(x[1])
print(x[1:3])
print(x[:3])
print(x[1:])


#manipulate list

fruit = ["pienaple","melon","apple","banana"]
print(fruit)
fruit.append("kiwi")
print(fruit)
fruit.insert(0,"orange")
print(fruit)
fruit.insert(4,"peach")
print(fruit)
fruit.remove("peach") # remove for remove value of the list
print(fruit)
fruit.pop(0) # pop command just for index the value
print(fruit)
fruit[1]="strawberry"
print(fruit)

#  TUPLE

fullname = ("wahyu", "luna", "Wijaya")

def confert_second(second):
    hours = second // 3600
    minutes = (second - hours *3600)//60
    remain = second - hours * 3600-minutes*60
    return hours,minutes,remain
    
result = confert_second(5000)
print(type(result))
print(result)
hours,minutes,remain = result
print(hours,minutes,remain)

def file_size(file_info):
	file_name, file_type, file_size= file_info
	return("{:.2f}".format(file_size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21



animals = ["lion","zebra","dolphin","monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
print(f"total character {chars}, average length {chars/len(animal):.2f}")


winners = ["ashley","dylan","reese"]
for index, person in enumerate(winners):
    print("{}-{}".format(index+1, person))

def full_emails (people):
    result=[]
    for email,name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_emails([("luna@gmail.com","wahyu luna"),("asep12@yahoo.com","asep")]))


names = ["luna","wahyu","asep","wijaya"]
name = [len(name) for name in names]
print(name)

multiple = [x*7 for x in range(1,10)]
print(multiple)

z = [x for x in range(1,101) if x % 3 == 0]
print(z) 

def odd_numbers(n):
	return [x for x in range(1,n+1) if x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

#============================================================

### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)]) 



### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)


### List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines 
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])

### Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)


def squares(start, end):
    return [start*start for start in range(start,end+1)] 


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# This block of code changes the year on a list of dates.
# The "years" list is given with existing elements. 
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]


# The variable "updated_years" is initialized as a list data type 
# using empty square brackets []. This list will hold the new list
# with the updated years. 
updated_years = []

# The for loop checks each "year" element in the list "years".
for year in years:

    # The if-statement checks if the "year" element ends with the 
    # substring "2023". 
    if year.endswith("2023"):

        # If True, then a temporary variable "new" will hold the 
        # modified "year" element where the "2023" substring is 
        # replaced with the substring "2024".
        new = year.replace("2023","2024")

        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(new)
        
    # If False, the original "year" element will be appended to the 
    # the "updated_years" list unchanged.
    else:
        updated_years.append(year)


print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

# This list comprehension creates a list of squared numbers (n*n). It
# accepts two integer variables through the function’s parameters.
def squares(start, end):
    
# The list comprehension calculates the square of a variable integer 
# "n", where "n" ranges from the "start" to "end" variables inclusively.
# To be inclusive in a range(), add +1 to the end of range variable.
    return [n*n for n in range(start,end+1)] 


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a 
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block. 

# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]


print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the 
# element and adds a dash between the element and the moved character. 
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.
def change_string(given_string):

# Initialize "new_string" as a string data type by using empty quotes.
    new_string = ""
    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:

        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items: 
        # + Each list "element" (starting at index position [1:]), 
        # + a dash "-", 
        # + append the first character of the "element" (using the index 
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-"  + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string


print(change_string("1one 2two 3three 4four 5five")) 
# Should print "one-1 two-2 three-3 four-4 five-5"  

# This function accepts a list name and a list of elements, and returns
# a string with the format: "The "list_name" list includes: element1, 
# element2, element3". 
def list_elements(list_name, elements):

    # This task can be completed in a single line of code. The 
    # concatenation of strings, "list_name", and the list "elements" can
    # occur on the return line. In this case, the string "The " is added 
    # to the "list_name", plus the string " list includes: ", then the
    # "elements" are joined using a comma to separate each element of the 
    # list.
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"])) 
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"



