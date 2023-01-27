import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (id INTEGER, nombre TEXT, precio INTEGER)")

lista_de_productos = [ (1,'Impresora',300), (2,'Raton',20), (3,'Ordenador',600) ]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", lista_de_productos)

conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")

productos = cursor.fetchall()

for producto in productos:
    print(producto)

conexion.close()




