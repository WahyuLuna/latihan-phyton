# return dapat dalam bentuk list []

def kuadrat(argument):
    total = argument**2
    print(f"total kuadrat dari {argument} adalah {total}")
    return total  #agar hasil dari total di masukan menjadi nilai a
    
a = kuadrat(5)
print(a)

#fungsi dengan menggunakan return value dandan mutiiple argument

def tambah(argument1,argument2):
    total= argument1 + argument2
    print(f"hasil {argument1} + {argument2} = {total}")
    return total

a = tambah (3,4)
print(a)

def kali(argument1,argument2):
    total= argument1 * argument2
    print(f"hasil {argument1} * {argument2} = {total}")
    return total

a = tambah (3,4)
print(a)
b = kali (3,a)
print(b)








