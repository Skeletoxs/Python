import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES ('Abraham','Zambrano','Varela',25)")

conexion.commit()

conexion.close()