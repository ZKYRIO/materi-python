def pilihanUser():
    pilihan_user = int(input("Masukkan pilihan anda : "))
    while pilihan_user > 2:
        pilihan_user = int(
            input("Opsi tidak ditemukan, Masukkan pilihan anda kembali : "))
    if (pilihan_user == 1):
        segitiga()
    if (pilihan_user == 2):
        persegi()

def segitiga():
    print("================================")
    print("Program menghitung luas segitiga")
    print("================================")
    alas = int(input("Masukkan besar alas : "))
    tinggi = int(input("Masukkan besar tinggi : "))
    L = 1/2 * alas * tinggi
    print("Luas segitia adalah", L)

def persegi():
    sisi = int(input("Masukkan besar sisi : "))
    L = sisi * 4
    print("Luas persegi adalah ", L)


print("Macam - Macam Program Perhitungan")
print("1. Segitiga")
print("2. Persegi")
print("\n")
pilihanUser()