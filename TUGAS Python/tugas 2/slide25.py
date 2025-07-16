#ubah infix menjadi postfix
from ArrayStack import *

#memeriksa precedence
def f(c):
    if c in ('+','-'):
        return 1
    else:
        if c in ('*','/'):
            return 2
        else:
            if c == '#':
                return 0
            else:
                return 3

#memeriksa ranking
def r(c):
    if c in ('+','-'):
        return -1
    else:
        if c in ('*','/'):
            return -1
        else:
            if c == '#':
                return 0
            else:
                return 1
S=ArrayStack()
S.push('#')
infix = input('Masukkan notasi infix diakhiri # : ')
current = infix[0]
polish=''
idx=0
rank=0
while (current != '#'):
    if S.is_empty():
        print('Invalid, stack kosong')
        break
while (f(current) <= f(S.top())):
    temp = S.pop()
    polish = polish + temp
    rank = rank + r(temp)
    S.push(current)
    idx=idx+1
    current=infix[idx]
    if (rank < 1):
        print('invalid infix !')
        break

while (S.top() != '#'):
    temp = S.pop()
    polish = polish + temp
    rank = rank + r(temp)
    if rank < 1:
        print('Invalid !!')
        break
if (rank==1):
    print('Valid-polish : ')
    print(polish)
else:
    print('Invalid result')
