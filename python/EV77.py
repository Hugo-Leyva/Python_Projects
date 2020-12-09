import sqlite3

conexion=sqlite3.connect("bdpa.db")
codigo=int(input("Ingresa el codigo del articulo"))
cursor=conexion.execute("select descripcion, precio from articulos where codigo=?", (codigo,))
fila=cursor.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existe el articulo con dicho codigo")
conexion.close()

