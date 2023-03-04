# rumus luas trapesium = 1/2*(a+b)*t
# rumus keliling jajar genjang = 2*(a+b)
# rumus volume kerucut = 1/3*phi*r*r*t

print("Program Luas Trapesium")
print("==================================")
a = int(input("Masukkan Nilai Alas a : "))
b = int(input("Masukkan Nilai Alas b : "))
t = int(input("Masukkan Nilai Tinggi : "))
LTrap = 1/2*(a+b)*t
print("===================================")
print("Luas Trapesium Adalah : ", LTrap)
print("=====================================")
print("Program Keliling Jajar Genjang")
print("=====================================")
c = int(input("Masukkan Sisi C : "))
d = int(input("Masukkan Sisi D : "))
Kjar = 2*(c+d)
print("=====================================")
print("Keliling Jajar Genjang : ", Kjar)
print("=====================================")
print("Program Volume Kerucut")
print("======================================")
phi = 3.14
r = int(input("Masukkan Nilai r : "))
tinggi = int(input("Masukkan Nilai Tinggi : "))
Vker = 1/3*phi*r*r*tinggi
print("=====================================")
print("Volume Kerucut Adalah : ", Vker)
print("=====================================")
