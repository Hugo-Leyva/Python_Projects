import sqlite3

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect("C:/Users/hugo_/Desktop/cosas/Python/bdpa.db")
        return conexion

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into clientes1(nombre, edad, medicamento) values (?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()


    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, edad, medicamento from clientes1 where nombre=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, edad, medicamento from clientes1"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from clientes1 where nombre=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update clientes1 set nombre=?, edad=?, medicamento=? where nombre=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()
