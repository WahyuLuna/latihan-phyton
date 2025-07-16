
while True :
    print ("========================================")
    print ("program memeriksa angka bilangan  prima\n")
    data = int(input("Masukan angka :"))

    hasil = data%2
    print ("\n=======(HASIL)=======")
    if hasil == 1:
        print ("\nini bilangan prima")
        
    else :
        print("\nini bukan bilangan prima")
        
    jawab = int(input("apakah masih ingin di ulang [Y=1 / N=0]: "))  
    
    if jawab == 1 :
        continue
    else :
        print("Terimkasih")
