print("Macam - Macam Program Perhitungan")
print("1. Segitiga")
print("2. Persegi")
print("\n")
pilihan_user = input("Masukkan pilihan anda : ")

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
    print(L)
