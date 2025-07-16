import sqlite3#menginport library mysqllite

conn=sqlite3.connect("db_1.1.db")#membuat data base
#apabila dsta base tidak ditemukan maka program akan otomatis membuat data base yang baru


cur = conn.cursor()

data=[
    ("P1","matematika","sinar mas","asep",2016),
    ("P2","Fisika","CNN","kipli",2013),
    ("P3","Kimia","fajar publish","dudung",2010),
    ("P4","Python","sinar mas","wahyu",2022),
    ("P5","Sejarah","fajar publish","dimas",2000),
    ("P6","Sqllite3","sinar mas","agung",2015)
]
#menginput data
try:
    dml="INSERT INTO BUKU VALUES(?,?,?,?,?)"
    cur.executemany(dml,data)
    print("berhasil")
except:
    print("gagal")