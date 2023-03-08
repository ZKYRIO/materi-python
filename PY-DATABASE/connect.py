import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

if database.is_connected():
    print("Berhasil terhubung dengan database")