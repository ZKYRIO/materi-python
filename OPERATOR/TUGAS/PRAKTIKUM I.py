cels = int(input("masukkan suhu (dalam suhu) :"))
ream = cels*0.8
farnh = (cels*1.8)+32
kelv = cels + 273.15
print("== == == == == == == == == == == PROGRAM KONVERSI SUHU == == == == == == == == == ==")
print("Celsius || "+"Reamur       || " +
      "farenheit         || "+"Kelvin        ||")
print("====================================================================================")
print(format(cels) + "      ||", format(ream) + "         ||",
      format(farnh) + "              ||", format(kelv) + "        ||")
