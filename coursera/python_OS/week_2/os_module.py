import os


#delete file
# os.remove("test.txt")


#change the name file
#os.rename("main.py","main.txt")

#check the file is exist or not
# print(os.path.exists('main.txt'))
# print(os.path.exists('main.py'))

# to get the size of file
# print(os.path.getsize("data.txt"))

# to know when tha data was made
# import datetime
# date =os.path.getatime("data.txt") 
# print(datetime.datetime.fromtimestamp(date))

#to know where the file are on
# print(os.path.abspath("data.txt"))

# command to make new folder
# print(os.getcwd())

# # make new folder
# os.mkdir("new_text")
# os.chdir("new_text")
# print(os.getcwd())

# # delete directory
# os.mkdir("new_text")
# os.rmdir("new_text")
# print(os.getcwd())

# to know inside the directory
print(os.listdir("new_text"))



