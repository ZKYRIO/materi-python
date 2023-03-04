print("=====================================")
print("      Toko Jaya Abadi Sejahtera     ")
print("=====================================")
print("Tanggal   : 14 / 11 / 2022")
print("Kasir     : Muhamad Rizky Hamdani")
print("Pelanggan : Lovrinka Damara")
print("=====================================")
total = int(input("Total Belanja Anda : Rp "))
if (total > 300000):
    print("Potongan Harga : 30%")
    print("Total yang harus di bayar adalah : ","Rp", total - (total * 30/100))
elif (100000 < total < 300000):
    print("Potongan Harga : 15%")
    print("Total yang harus di bayar adalah : ","Rp", total - (total * 15/100))
elif (50000 < total < 100000):
    print("Potongan Harga : 2%")
    print("Total yang harus di bayar adalah : ", "Rp", total - (total * 2/100))
else:
    print("Total yang harus di bayar adalah : ", "Rp", total)

print("\n")
