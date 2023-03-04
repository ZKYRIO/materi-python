nama = ['Zakariya', 'Yudi', 'Anggi', 'Yudha', 'Anggun','Baskoro']
namaYangDicari = input("Masukkan Nama Yang dicari = ")
for i, nm in enumerate(nama):
    if(nm.lower() == namaYangDicari.lower()):
        print("Nama Yang Anda Cari Ada di Indeks ke -", i)
        break
else :
    print("Nama Yang Anda Cari Tidak Ditemukan!!!")