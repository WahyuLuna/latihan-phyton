class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0
 
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if return_city.population < min_population:
		return_city = city1.name
 
	if return_city.name:
		return return_city.name
	else:
		return "dfhdf"

print(max_elevation_city(100000)) 
 
 
 
 
 
 
 