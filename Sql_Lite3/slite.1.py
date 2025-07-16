import sqlite3#menginport library mysqllite

conn=sqlite3.connect("db_1.1.db")#membuat data base
#apabila dsta base tidak ditemukan maka program akan otomatis membuat data base yang baru


cur = conn.cursor()
table = """
        CREATE TABLE BUKU(
            KODE CHAR(20) NOT NULL PRIMARY KEY,
            JUDUL VARCHAR(50),
            PENERBIT VARCHAR(50),
            PENULIS VARCHAR(50),
            TAHUN INTEGER
        )
"""
cur.execute(table)