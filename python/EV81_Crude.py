import sqlite3

class Articulos:

    def abrir(self): #ABRIR LA BASE DE DATOS
        conexion=sqlite3.connect("C:/Users/hugo_/Desktop/cosas/Python/bdpa.db")
        return conexion

    def alta(self,datos): #INSERTAR REGISTROS EN UNA TABLA
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into Laboratorio2(nombre, telefono) values (?,?)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close

    def consulta(self,datos):  #CONSULTAR DATOS DE UNA TABLA
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, telefono from Laboratorio2 where codigo=?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self): #PARA RECUPERAR/CONSULTAR TODOS DE TABLAS
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo, nombre, telefono from Laboratorio2"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self,datos): #ELIMINAR UN ARTICULO SEGUN EL CODIGO QUE LE DE
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from Laboratorio2 where codigo=?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()

    def modificacion(self,datos): #PERMITE MODIFICAR LA BASE DE DATOS
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update Laboratorio2 set nombre=?, telefono=? where codigo=?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
