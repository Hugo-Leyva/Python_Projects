import sqlite3

conexion=sqlite3.connect("bdpa.db")

cursor=conexion.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()
