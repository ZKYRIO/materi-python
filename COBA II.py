month = ("Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember")
bulan = int(input("Masukkan Bulan : "))
if (bulan>=1) and (bulan<=12) :
    print("Bulan ke",bulan,"Adalah bulan", month[bulan])
else :
    print("GAK NOK BULAN IKU COYY")