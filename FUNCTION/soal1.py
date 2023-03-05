def pilihanUser():
    pilihan_user = int(input("Masukkan pilihan anda : "))
    if (pilihan_user == 1):
        segitiga()
    elif (pilihan_user == 2):
        persegi()
    elif (pilihan_user == 3):
        persegiPanjang()
    elif (pilihan_user == 4):
        lingkaran()
    elif (pilihan_user == 5):
        jajarGenjang()
    else:
        print("\nOpsi tidak ditemukan, mohon pilih kembali !!")
        pilihanUser()


def pilihanYoN():
    pilihan_user = input("Apakah anda ingin memilih kembali (y/n) : ")
    if (pilihan_user == "y"):
        pilihanUser()
        pilihanYoN()
    else :
        pilihan_user = input("konfirmasi pilihan anda, Apakah anda ingin memilih lagi ? (y/n) : ")
        if (pilihan_user == "y"):
            pilihanUser()
        if (pilihan_user == "n"):
            print("Terima Kasih")
        else:
            print("Terima Kasih")

def segitiga():
    print("================================")
    print("Program menghitung luas segitiga")
    print("================================")
    alas = int(input("Masukkan besar alas : "))
    tinggi = int(input("Masukkan besar tinggi : "))
    L = 1/2 * alas * tinggi
    print("Luas segitia adalah", L)

def persegi():
    print("================================")
    print("Program menghitung luas persegi")
    print("================================")
    sisi = int(input("Masukkan besar sisi : "))
    L = sisi * 4
    print("Luas persegi adalah ", L)

def persegiPanjang():
    print("================================")
    print("Program menghitung luas persegi panjang")
    print("================================")
    panjang = int(input("Masukkan besar panjang: "))
    lebar = int(input("Masukkan besar lebar: "))
    L = panjang * lebar
    print("Luas persegi panjang adalah",L)

def lingkaran():
    print("================================")
    print("Program menghitung luas lingkaran")
    print("================================")
    phi = 3.14
    r = int(input("Masukkan besar jari jari: "))
    L = phi * r * r
    print("Luas lingkaran adalah", L)

def jajarGenjang():
    print("================================")
    print("Program menghitung luas jajar genjang")
    print("================================")
    alas = int(input("Masukkan besar alas: "))
    tinggi = int(input("Masukkan besar tinggi: "))
    L = alas * tinggi
    print("Luas jajar genjang adalah", L)

print("Macam - Macam Program Perhitungan")
print("1. Segitiga")
print("2. Persegi")
print("3. Persegi Panjang")
print("4. Lingkaran")
print("5. Jajar Genjang")
print("\n")
pilihanUser()
pilihanYoN()