print("Program If")
print("================")
x = int(input("Masukkan bilangan : "))

if (x > 0):
    print(x, "adalah bilangan positif")

print("\a")

print('Program IF ELSE')
print("======================")
y = int(input("Masukkan bilangan : "))
if (y > 0):
    print(y, "adalah bilangan positif")
else:
    print(y, "adalah bilangan negatif")

print('\n')

print("Program ELIF")
print("=====================")
z = int(input("Masukkan Bilangan : "))
if (z > 1000):
    print(z, "Adalah bilangan lebih dari 1000")
elif (z > 200):
    print(z, "Adalah bilangan lebih dari 200")
else:
    print(z, "Adalah bilangan kurang dari 200")
