# KOMPARASI DAN LOGIKA 

#++++++3-------10+++++

inputUser = float(input ("masukan anghka yang bernilai \n kurang dari 3 \n atau \n lebih dari 10 \n : "))

#++++++3---------------
iskurangdari = (inputUser < 3)
print("kurang dari 3 :",iskurangdari)

#-----------------10+++++++++
islebihdari = (inputUser > 10)
print("lebih dari 10 :",islebihdari)

#+++++++++3---------10+++++++++
iscorrect = iskurangdari or islebihdari
print ("angka yang anda masukan :", iscorrect)


#-----3++++++++++10--------

inputUser = float(input ("masukan anghka yang bernilai \n lebih dari 3 \n atau \n kurang dari 10 \n : "))

#--------3+++++++
islebihdari = (inputUser > 3)
print("lebih dari 3 :",islebihdari)

#+++++++++10-------
islkurangdari = (inputUser < 10)
print("kurang dari 10 :",islkurangdari)


#----3++++++++10---------
iscorrect = iskurangdari or islebihdari
print ("angka yang anda masukan :", iscorrect)

#latihan soal : -------0++++++5---------10++++++++20------------------------

print("akan ditentukan apakah angka anda \n lebih dari nol \n kurang dari 5 \n lebih dari 10 \n kurang dari 20")
angkauser = float(input("masukan angka : "))

lebihdari0 = (angkauser > 0)
kurangdari5 = (angkauser < 5)
lebihdari10 = (angkauser > 10)
kurangdari20 = (angkauser < 20)

kesimpulan = lebihdari0 or kurangdari5 or lebihdari10 or kurangdari20

print ("apakag akngka anda lebih dari 0",lebihdari0 )
print ("apakah akngka anda kurang dari 5",kurangdari5 )
print ("apakag akngka anda lebih dari 10",lebihdari10 )
print ("apakah akngka anda kurang dari 20",kurangdari20 )

print("kesimpulan angka anda : ", kesimpulan)























