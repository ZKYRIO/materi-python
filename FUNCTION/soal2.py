d1 = 0
d2 = 1

banyak = int(input("Masukkan Jumlah Deret Fibonacci : "))
print("-"*35)
print("Bilangan Fibonacci :")

for x in range(banyak):
    print(d2)
    cn = d1 + d2
    d1 = d2
    d2 = cn