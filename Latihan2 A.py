tinggi = float(input("Masukan Tinggi Badan (meter):"))
BMI = float(input("Masukan BMI (meter):"))
def hitungBB(tinggi,BMI):
     BB = BMI*(tinggi**2)
     return (BB)
BB = hitungBB(tinggi,BMI)
print("Berat badan yang diperlukan", BMI, "adalah", round(BB,2),"Kg")
