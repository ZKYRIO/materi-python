import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko"
)

d_name = []
d_alamat = []

data = int(input("Masukkan jumlah data yang ingin anda masukkan : "))

for x in range(data):
    nama = input("Masukkan nama anda : ")
    d_name.append(nama)
    alamat = input("Masukkan alamat tempat tinggal anda : ")
    d_alamat.append(alamat)

cursor = db.cursor()
sql = "INSERT INTO pelanggan (nama, alamat) VALUE (%s,%s)"

for i in range(data):
    val = (d_name[i], d_alamat[i])
    cursor.execute(sql,val)

db.commit()

print("{} data di tambahkan".format(len(val)))