import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko"
)

nama = input("Masukkan nama anda : ")
alamat = input("Masukkan alamat tempat tinggal anda : ")

cursor = db.cursor()
sql = "INSERT INTO pelanggan (nama, alamat) VALUE (%s,%s)"
val = (nama,alamat)
cursor.execute(sql,val)

db.commit()

print("{} data di tambahkan".format(cursor.rowcount))