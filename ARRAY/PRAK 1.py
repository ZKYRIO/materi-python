nama = input("Masukkan Nama Anda : ")
y = int(input("Masukkan jumlah elemen : "))

nilai = []
total = 0
for x in range(y):
    bil = int(input("Masukkan Nilai ke- {} : ".format(x+1)))
    nilai.append(bil)
    total = total + nilai[x]
print(nilai)

print()
print("Program Memasukkan Nilai Ke Dalam Array")
print("=========================================")
print("By : ",nama)
print("=========================================")
print("Rata - rata nilai anda adalah ", total / y)