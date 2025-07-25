


def email_list(domains):
    emails=[] 
    for domain,name in domains.items():
        for name in name:
            emails.append(name+" "+domain)
    return (emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# def email_list(domains):
# 	emails = []
# 	for users in domains:
# 	  for user in users:
# 	    emails.append(user)
#     print(emails)
  
# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))




# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	for resource_group, resources in group_dictionary.items():
# 		for resource in resources:
#             if resource in user_groups:
#                 user_groups[resource].append(resource_group)
#             else:
#                 user_groups[resource] = [resource_group]

# 	return(user_groups)

# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))


def groups_per_user(group_dictonary):
    user_group = {}
    for rg,rs in group_dictonary.items():
        for r in rs:
            if r in user_group:
                user_group[r].append(rg)
            else:
                user_group[r] = [rg]
                
    return user_group

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))




def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for key,value in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += basket[key]
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44



wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)