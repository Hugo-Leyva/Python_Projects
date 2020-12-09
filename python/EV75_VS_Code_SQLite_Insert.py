import sqlite3

conexion=sqlite3.connect("bdpa.db")

conexion.execute("insert into articulos (descripcion,precio) values (?,?)", ("refresco", 35.50))
conexion.execute("insert into articulos (descripcion,precio) values (?,?)", ("fritos", 12.50))
conexion.execute("insert into articulos (descripcion,precio) values (?,?)", ("galletas",8.50))

conexion.commit()       #los signos de ?,? son parametros son los datos que le vamos a dar a la tabla segun los campos (los signos son las posiciones) 
conexion.close          #por ejemplo para descripcion y corresponen refresco y 25.50