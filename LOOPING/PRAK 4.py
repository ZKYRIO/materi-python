# PROGRAM MENAMPILKAN SUHU DALAM C,R,K

suhu1 = int(input("Masukkan Suhu Awal Dalam Celsius  : "))
suhu2 = int(input("Masukkan Suhu Akhir Dalam Celsius : "))
# K = C + 273
# R = 4/5 * C
# F = C * 1.8 + 32
for x in range(suhu1,suhu2,5):
    K = x + 273
    R = 4/5 * x
    F = x * 9/5 + 32
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("Celsius   ||  Farenheit   || Reamur   ||  Kelvin")
    print("----------------------------------------------------")
    print(x,"        ||   ",F,"      ||  ",R,"    ||  ",K)