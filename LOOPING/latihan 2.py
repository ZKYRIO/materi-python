# PROGRAM MENENTUKAN BILANGAN GANJIL

x = int(input("Masukkan Bilangan Ganjil : "))

while x % 2 == 0:
    x = int(input("Bukan Bilangan Ganjil, Silahkan Ulangi Lagi !!"))
print("Benar",x,"adalah bilangan ganjil")