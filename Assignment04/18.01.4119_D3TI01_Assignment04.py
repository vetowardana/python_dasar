print("-----------------------------------")
print("Assignment 04")
print("-----------------------------------")
print("Aplikasi penghitung Body Mass Index (BMI)")
print(" ")

tb = input("Masukkan tinggi (cm) = ")
bb = input("Masukkan berat (kg)  = ")
print(" ")

x = float(tb)
a = x/100
b = float(bb)

try:
    hasil = b/a**2
except ZeroDivisionError:
    hasil = 0

if(a > 0.0 and b > 0):
    if(hasil < 18.5):
        print("Hasilnya :")
        print("Status berat : kekurangan berat badan")
        print("Besaran BMI  :", hasil)
    elif(18.5 <= hasil <= 24.9):
        print("Hasilnya :")
        print("Status berat : normal(ideal)")
        print("Besaran BMI  :", hasil)
    elif(25.0 <= hasil <= 29.9):
        print("Hasilnya :")
        print("Status berat : kelebihan berat badan")
        print("Besaran BMI  :", hasil)
    elif(hasil >= 30.0):
        print("Hasilnya :")
        print("Status berat : obesitas")
        print("Besaran BMI  :", hasil)
else:
    print("Input tidak boleh kurang dari sama dengan 0!")
