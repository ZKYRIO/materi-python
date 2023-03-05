def faktor(x):
    if(x == 1):
        return 1
    else:
        return x * faktor(x-1)

print("\nPROGRAM MENGHITUNG FAKTORIAL")
print("="*30)
input_user = int(input("Masukkan bilangan positif: "))
print(input_user,"! = ",faktor(input_user))