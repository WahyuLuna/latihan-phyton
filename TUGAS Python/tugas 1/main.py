nama = input("Masukan Kata yang akan di urutkan : ")
a = []
a.extend(nama)
n = len(a)
total_step = 0
tukar = False
for i in range(n-1):
    print('\n=A=A=A=A=A=A=A=A=A=A=A=A=A=A=\n')
    print(f"nilai i={i},dan lebih kecil dari n = {n-1}")
    tukar = False
    print(f" pada putaran A = {i+1},Tukar = {tukar}")
    
    
    for j in range(n-i-1):
        print('\n\n=B=B=B=B=B=B=B=B=B=B=B=B=B=B=\n')
        print(f"nilai j = {j}, pada putaran B = {j+1},Tukar = {tukar}, nilai kondisi ={n-i-1} ")
        print('karena nilai diatas terpenuhi selanjutnya kita masuk ke perulangan')
        
        if a[j] > a[j+1]:
            print('karena nilai diatas terpenuhi selanjutnya kita masuk ke kondisi')
            
            print(f"\nB== nilai a[j]/index ke{j}={a[j]}, dan lebih besar dari pada nilai a[j+1]/indexke{j+1}={a[j+1]}")
            temp = a[j]
            print(f"\nB== nilai temp={a[j]}")
            print(f'nilainya diambil dari  a[{j}]')
            a[j] = a[j+1]
            print(f"\nB== nilai a[j]={a[j]}")
            print(f'nilainya diambil dari  a[j+1]/a index ke {j+1}')
            a[j+1] = temp
            print(f"\nB== nilai a[j+1]={a[j+1]}")
            print(f'nilainya diambil dari temp/{temp}')
            tukar = True
            print('nilai tukar menjadi True')
        else :
            print(f'\nkarena a[{j}]/{a[j]} lebih kecil dari a[{j+1}]{a[j+1]}\n, kodisi kita lewatkan\n')
            
        print('\nmaka hasil urutanya\n')
        print(a)
        j+=1
        total_step +=1
        print('nilai j kita tambah 1')     
            
                      
    if not tukar:
        print('tukar sama dengan True maka kita break')
        break
    i+=1
    print('nilai i kita tambah 1')



print(f"\n\nList '{nama}' setelah diurutkan:", a)
print(f"\n\nTotal Langkah yang dilakukan = {total_step}")
