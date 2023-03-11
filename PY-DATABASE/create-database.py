import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

# if db.is_connected():
#     print("NYAMBUNG COKK!!!")

cursor = db.cursor()
cursor.execute("create database toko")

print("Database berhasil di buat")