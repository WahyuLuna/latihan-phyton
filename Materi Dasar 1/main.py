def replace(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+ old_domain)
        new_email = email[:index] +"@"+new_domain
        return new_email
    
print (replace("wa@gmail.com","gmail.com", "yahoo.com"))

def examp(name, grade):
    return "name : {}, with grade : {}".format(name, grade)

print (examp("wahyu",90))

def to_celcius(x):
    return (x-32)*5/7

for i in range(0,101,10):
    print("{:>3} f | {:>6.2f} C".format(i,to_celcius(i)))




