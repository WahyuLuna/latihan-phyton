number = 0
while number < 7:
    number +=1
    print(number)
    
print("#################################")    

def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0:
        result *= n
        n -= 1
    return result
    
print(factorial(9))

print("#################################")    

def rows_asr(rows):
    for x in range(rows):
        for y in range(x+1):    
            print("*", end="")
        print("")
        
rows_asr(5)

print("#################################")    

def coun(start):
    x = start
    if x > 0:
        rs = "count down to 0 :"
        while x > -1:
            rs += str(x)
            if x > 0:
                rs += ","
            x -= 1
    else:
        rs = " cant"
    return rs

print(coun(10))
print("#################################")    

def oddnumber(maxnum):
    rs = ""
    for i in range(1):
        a = 0
        if 0 < maxnum:
            rs = "Should Be"
            while i > 0:
                a += 2
                rs += str(a)
                
        else :
            rs = " Not Displayed"        
    return rs
        
         
print(oddnumber(10))

print("#################################")    
x = 1
sum= 5
while x <= 10:
    sum += x
    x += 1
    print(sum)
print("#################################")    

for x in range(1,10,3):
    print(x)
    


print("#################################")    
for x in range(10):
    for y in range(x):
        print(y)
print("#################################")

def count_toten():
    x = 1
    while x <= 10:
        print(x)
        x += 1
        
count_toten()    

print("#################################")

def digits(n):
    count = 0
    if n == 0:
        count += 1
    while n > 0:
        n //= 10
        count += 1
    return count

print(digits(25))
print(digits(245))
print(digits(2562))
print(digits(0))
    

print("#################################")
for x in range(1,6):
    print(x+1)
print("################erte#################")
num1 = 0
num2 = 0
for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y+3

print(num1+num2)
print("#################################")


