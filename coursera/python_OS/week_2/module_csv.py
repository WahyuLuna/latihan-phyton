import csv

# f = open("read.txt")
# csv_f = csv.reader(f)
# for row in csv_f:
#     name,phone,role =row
#     print(f"name :{name}, phone :{phone}, role :{role}")


# membaut file CSV
# host = [["workstation.local","192.168.25.46"],["webserver.cloud","10.2.5.6"]]
# with open('host.csv','w')as host_csv:
#     writer = csv.writer(host_csv)
#     writer.writerow(host)

# user=[{"name": "sol mansi", "user_name":"solm","department":"IT"},
#       {"name": "chalie grey", "user_name":"grey","department":"IT"},
#       {"name": "lio nelson", "user_name":"lion","department":"UI/UX"}]
# keys = ["name", "user_name", "department"]
# with open('by_deparment.csv','w')as by_deparment:
#     writer = csv.DictWriter(by_deparment, fieldnames=keys)
#     writer.writeheader()
#     writer.writerow(user)

# with open('software.csv') as software:
#     reader = csv.DictReader(software)
#     for row in reader:
#         print("{} has {}").format(row['name'],row['user'])

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

