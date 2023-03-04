# PROGRAM MENENTUKAN BILANGAN GANJIL GENAP SESUAI INPUT USER

bil1 = int(input("Masukkan Bilangan awal  : "))
bil2 = int(input("Masukkan Bilangan Akhir : "))
print("============================")
for x in range(bil1,bil2+1):
    if(x % 2 == 0 ):
        print("Bilangan genap adalah : ", x)

print("============================")
for y in range(bil1,bil2):
    if(y % 2 != 0 ):
        print("Bilangan ganjil adalah : ", y)