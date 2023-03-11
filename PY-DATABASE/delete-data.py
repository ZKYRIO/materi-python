import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko"
)

data = input("Masukkan ID Pelanggan yang ingin dihapus: ")
cursor = db.cursor()
sql = "DELETE FROM pelanggan WHERE id_pelanggan=%s"
val = (data, )
cursor.execute(sql,val)

db.commit()

print("{} Data berhasil dihapus".format(cursor.rowcount))