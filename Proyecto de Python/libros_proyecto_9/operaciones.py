import sqlite3

def conectar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, year INTEGER, isbn INTEGER)")
    conexion.commit()
    conexion.close()

def insertar(titulo,autor,year,isbn):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros VALUES (NULL,?,?,?,?)", (titulo,autor,year,isbn))
    conexion.commit()
    conexion.close()

def visualizar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def buscar(titulo='',autor='',year=0,isbn=0):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE titulo=? OR autor=? OR year=? OR isbn=?", (titulo,autor,year,isbn))
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def borrar(id):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?", (id,))
    conexion.commit()
    conexion.close()

def actualizar(titulo,autor,year,isbn,id):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo=?, autor=?, year=?, isbn=? WHERE id=?", (titulo,autor,year,isbn,id))
    conexion.commit()
    conexion.close()



#Prueba
#conectar()
#insertar("titulo1","autor1",2001,111111)
#insertar("titulo2","autor2",2002,222222)
#insertar("titulo3","autor3",2003,333333)
#resultados = visualizar()
#for resultado in resultados:
#    print(resultado)

#resultados = buscar(year=2003)
#for resultado in resultados:
#    print(resultado)

#borrar(2)
#resultados = visualizar()
#for resultado in resultados:
#    print(resultado)

#actualizar(titulo="titulo5",autor="autor5",year=2005,isbn=555555,id=3)
#resultados = visualizar()
#for resultado in resultados:
#    print(resultado)