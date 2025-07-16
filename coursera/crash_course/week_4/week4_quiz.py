def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word)> 0: 
        # Complete the return statement using a string operation.
        return len(word) 
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0


def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4


def sort_distance(distances):
    distances.sort() # Sort the list
    distances.reverse() # Reverse the list of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

def increments(start, end):
    return [n+2 for n in range(start,end+1)] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# def countries(countries_dict):
#     result = ""
#     # Complete the for loop to iterate through the key and value items 
#     # in the dictionary.
#     for result in countries_dict.items():
#         # Use a string method to format the required string.
#         print(result)
#         result += result[:2]
#     return result

# print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# # Should print:
# # ['Kenya', 'Egypt', 'Nigeria']
# # ['China', 'India', 'Thailand']
# # ['Ecuador', 'Bolivia', 'Brazil']

def check_guests(guest_list, guest):
  return guest_list.get(guest,0) # Return the value for the given key


guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2



def setup_gradebook(old_gradebook):
    new_gradebook = old_gradebook
    for keys,value in new_gradebook.items():
        new_gradebook[keys]=0
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}

car_make = "Lamborghini"
print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)


host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())














