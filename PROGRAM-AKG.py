# Program Menghitung AKG Pria

# Pria = 66 + (13.7 * BB) + (5 * TB) - (6.8 * usia)
# Wanita = 665 + (9.6 * BB) + (1.8 * TB) - (4.7 * usia)

print("========== Program Angka Kebutuhan Gizi ==========")
BB = int(input("Masukkan Berat Badan Anda : "))
TB = int(input("Masukkan Tinggi Badan Anda : "))
usia = int(input("Masukkan Usia Anda : "))
sex = input("Jenis Kelamin ( pria / wanita ) : ")
frekuensi = input("""=======================
sangat jarang (kurang dari 2 kali dalam seminggu)
jarang (1 - 3 kali perminggu)
cukup (3 - 5 kali perminggu)
sering (6 - 7 kali perminggu)
sangat sering (2 kali sehari)
================================8
Frekuensi Olahraga Harian Anda : """)
pria = 66 + (13.7 * BB) + (5 * TB) - (6.8 * usia)
wanita = 665 + (9.6 * BB) + (1.8 * TB) - (4.7 * usia)

print("==================================================")

if (sex == "pria", frekuensi == "sangat jarang") :
    print("Angka Kebutuhan Gizi Anda Adalah = ", pria * 1.2)
elif (sex == "wanita", frekuensi == "sangat jarang") :
    print("Angka Kebutuhan Gizi Anda Adalah = ", wanita * 1.2)
elif (sex == "pria", frekuensi == "jarang") :
    print("Angka Kebutuhan Gizi Anda Adalah = ", pria * 1.375)
elif (sex == "wanita", frekuensi == "jarang") :
    print("Angka Kebutuhan Gizi Anda Adalah = ", wanita * 1.375)
elif (sex == "pria", frekuensi == "cukup"):
    print("Angka Kebutuhan Gizi Anda Adalah = ", pria * 1.55)
elif (sex == "wanita", frekuensi == "cukup"):
    print("Angka Kebutuhan Gizi Anda Adalah = ", wanita * 1.55)
elif (sex == "pria", frekuensi == "sering"):
    print("Angka Kebutuhan Gizi Anda Adalah = ", pria * 1.725)
elif (sex == "wanita", frekuensi == "sering"):
    print("Angka Kebutuhan Gizi Anda Adalah = ", wanita * 1.725)
elif (sex == "pria", frekuensi == "sangat sering"):
    print("Angka Kebutuhan Gizi Anda Adalah = ", pria * 1.9)
elif (sex == "wanita", frekuensi == "sangat sering") :
    print("Angka Kebutuhan Gizi Anda Adalah = ", wanita * 1.9)
