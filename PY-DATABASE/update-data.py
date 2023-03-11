import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko"
)

cursor = db.cursor()
sql_show = "SELECT * FROM pelanggan"
cursor.execute(sql_show)

result = cursor.fetchall()
for data in result:
    print(data)

print("="*20)
def update():
    id_pelanggan = int(input("Masukkan nomor id pelanggan yang ingin di ubah: "))
    name = input("Masukkan perubahan nama: ")
    alamat = input("Masukkan perubahan alamat: ")
    sql_update = "UPDATE pelanggan SET nama=%s , alamat=%s WHERE id_pelanggan=%s"
    val = (name, alamat, id_pelanggan)
    cursor.execute(sql_update,val)
    db.commit()
    print("{} Data berhasil di update".format(cursor.rowcount))
update()

