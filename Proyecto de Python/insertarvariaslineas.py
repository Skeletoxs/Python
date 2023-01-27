import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

lista_personas = [ ('Pedro','Rodriguez','Perz',26), ('Maria','Lopez','Gomez',45), ('Luis','Gonzalez','Perez',46) ]

cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)

conexion.commit()

conexion.close()
