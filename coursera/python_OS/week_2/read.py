file = open("data.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

for i in lines:
    print(i)

# data inside data.txt will deleted if you run this code
# with open("data.txt", "w") as file:
#     file.write("hallo apa kabar")










