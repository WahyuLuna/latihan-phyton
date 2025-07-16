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