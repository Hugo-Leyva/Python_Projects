import sqlite3

conexion=sqlite3.connect("bdpa.db")

try:
    conexion.execute("""create table Almacen (
        codigo integer primary key autoincrement,
        nombre varchar(70),
        medicamento varchar(20)
    )""")
    print("se creo la tabla almacen")
except sqlite3.OperationalError:
    print("la tabla almacen ya existe")
conexion.close()