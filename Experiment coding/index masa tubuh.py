tinggi = float(input("masukan tinggi dalam cm : "))
berat = float(input("masukan berat dalam kg : "))

IMB = berat / (tinggi/100)**2
print (f"index tubuh mu = {IMB}")

if IMB <= 18.5:
    print("kurang sehat (kurus)")
elif IMB <= 24.9:
    print("sehat")
elif IMB <= 29.9:
    print("gemuk")
else:
    print("obesitas")
