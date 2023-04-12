deret = [0,1]

def fibonacci():
    for x in range(banyak):
        un = x
        un2 = x + 1
        jumlah = deret[un] + deret[un2]
        deret.append(jumlah)
    
    for y in range(banyak):
        print(deret[y+1])
        
banyak = int(input("Masukkan Jumlah Deret Fibonacci : "))
print("-"*35)
print("Bilangan Fibonacci :")
fibonacci()
