print("---------------------------------------------")
print("Assignment 03 Soal 1")
print("---------------------------------------------")
print(' ')
print("Aplikasi penghitung fungsi : 2x\N{SUPERSCRIPT THREE} + 2x + 15/x")
print(' ')
x = input("Masukkan nominal X : ")
print(' ')

a = int(x)
pangkat = 2*a**3
kali = 2*a
bagi = 15/a

hasil = pangkat + kali + bagi

print("Jawaban :")
print("2x\N{SUPERSCRIPT THREE} + 2x + 15/x")
print("=" + " 2" + "(" + x + ")\N{SUPERSCRIPT THREE}" " + " + "2" + "(" + x + ")" " + " + "15" + "/" + x)
print("=", pangkat, "+", kali, "+", bagi)
print('= ', hasil)
