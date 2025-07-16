    # Dictonary

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d

h = histogram('dinosaurus')
print(h)
print(h['a'])
print(h['u'])

    # Tuple

t = ('a', 'b', 'c', 'd', 'e', 'f')
print(t)
print(t[0]) 
print(t[1]) 


    
    