def fibonacci() :
    bil1 = 0
    bil2 = 1
    for bilangan in range(banyak):
        print (bil2)
        F = bil2 + bil1
        bil1 = bil2
        bil2 = F

banyak = int(input("Masukkan Jumlah Deret Fibonacci : "))
print("-"*35)
print("Bilangan Fibonacci :") 
fibonacci()