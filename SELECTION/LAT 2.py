print("Program menentukan 2 bilangan positif / negatif")
print("==================================================")
x = int(input("Masukkan bilangan 1 : "))
y = int(input("Masukkan bilangan 2 : "))

if (x > 0 and y > 0):
    print("Kedua bilangan tersebut adalah bilangan POSITIF")
elif (x > 0 or y > 0):
    print("Salah satu bilangan tersebut adalah bilangan NEGATIF ")
else:
    print("Kedua bilangan tersebut adalah bilangan NEGATIF")
