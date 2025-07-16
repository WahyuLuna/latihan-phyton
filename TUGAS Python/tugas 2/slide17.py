from ArrayStack import *
S = ArrayStack()
kalimat = input('Masukkan Satu Kalimat : ')
panjang = len(kalimat)

for c in kalimat:
    S.push(c)
x = ''
for i in range(panjang):
    x = x + S.pop()

print('Baca Terbalik : ')
print(x)
