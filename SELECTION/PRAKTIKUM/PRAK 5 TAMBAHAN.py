print("=====================================")
produk1 = input("Barang    : ")
qty1 = int(input("qty       : "))
harga1 = int(input("harga     : "))
total1 = qty1 * harga1
print("=====================================")
produk2 = input("Barang   : ")
qty2 = int(input("qty      : "))
harga2 = int(input("harga    : "))
total2 = qty2 * harga2
print("=====================================")
produk3 = input("Barang   : ")
qty3 = int(input("qty      : "))
harga3 = int(input("harga    : "))
total3 = qty3 * harga3
print("=====================================")
produk4 = input("Barang   : ")
qty4 = int(input("qty      : "))
harga4 = int(input("harga    : "))
total4 = qty4 * harga4
print("=====================================")
produk5 = input("Barang   : ")
qty5 = int(input("qty      : "))
harga5 = int(input("harga    : "))
total5 = qty5 * harga5


print("=====================================")
print("      Toko Jaya Abadi Sejahtera     ")
print("=====================================")
print("Tanggal   : 14 / 11 / 2022")
print("Kasir     : Muhamad Rizky Hamdani")
print("Pelanggan : Lovrinka Damara")
print("=====================================")
print("||" "   Produk    " "||" "    quantity    " "||" "   Harga   " "||" "   Total   " "||")
print(" ", produk1, "        ", qty1,"          ", harga1, "     ", total1)
print(" ", produk2, "       ", qty2,"          ", harga2, "     ", total2)
print(" ", produk3, "      ", qty3,"          ", harga3, "     ", total3)
print(" ", produk4, "       ", qty4,"          ", harga4, "     ", total4)
print(" ", produk5, "      ", qty5,"          ", harga5, "     ", total5)
print("=====================================")
Total = total1 + total2 + total3 + total4 + total5
print("Total Belanja adalah = ", Total)
if (Total > 300000):
    print("Potongan Harga : 30%")
    print("Total yang harus di bayar adalah : ",
          "Rp", Total - (Total * 30/100))
elif (100000 < Total < 300000):
    print("Potongan Harga : 15%")
    print("Total yang harus di bayar adalah : ",
          "Rp", Total - (Total * 15/100))
elif (50000 < Total < 100000):
    print("Potongan Harga : 2%")
    print("Total yang harus di bayar adalah : ", "Rp", Total - (Total * 2/100))
else:
    print("Total yang harus di bayar adalah : ", "Rp", Total)

print("\n")
