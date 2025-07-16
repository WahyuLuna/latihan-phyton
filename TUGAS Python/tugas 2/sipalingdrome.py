#palindrome
from ArrayStack import *
from ArrayQueue import *
import string

S=ArrayStack()
Q=ArrayQueue()
kalimat = input('Masukkan sebuah kalimat : ')
kalimat=kalimat.lower()
m = len(kalimat)
for c in kalimat:
	if (c.isalpha() or c.isdigit()):
		S.push(c)
		Q.enqueue(c)

palin = True

for i in range(m):
    if (not S.is_empty()):
        x1 = S.pop()
        x2 = Q.dequeue()
        if (x1 != x2):
            palin = False
            break

if (palin == True):
    print(kalimat,': palindrome')
else:
    print(kalimat, ': bukan palindrome')

