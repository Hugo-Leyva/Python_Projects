import sqlite3

conexion=sqlite3.connect("bdpa.db")

try:
    conexion.execute("""create table hora_tab (
        hora TIME,
        hora2 varchar(40)
    )""")
    print("se creo la tabla correo")
except sqlite3.OperationalError:
    print("la tabla correo ya existe")
conexion.close()

