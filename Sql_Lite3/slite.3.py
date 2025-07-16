import sqlite3#menginport library mysqllite

conn=sqlite3.connect("db_1.1.db")#membuat data base
#apabila dsta base tidak ditemukan maka program akan otomatis membuat data base yang baru


cur = conn.cursor()

cur.execute("SELECT JUDUL FROM BUKU")

result = cur.fetchall()

print (result)