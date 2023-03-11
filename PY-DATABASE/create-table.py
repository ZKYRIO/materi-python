import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "toko"
)

cursor = db.cursor()
table = """ CREATE TABLE pelanggan (
    id_pelanggan INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255),
    alamat VARCHAR(255)
)"""

cursor.execute(table)

print("Tabel pelanggan berhasil di buat")
