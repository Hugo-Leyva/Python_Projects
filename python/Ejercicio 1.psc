Algoritmo AreaTriangulo
	Definir numopcion,altura,base, lado Como Entero
	definir areaa Como Real
	Escribir "que area desea calcular? ingrese el numero de la opcion. 1-. Triangulo 2-. Cuadrado:"
	Leer numopcion
	si numopcion < 2 Entonces
		Escribir "ingresa la base del triangulo:"
		leer base
		Escribir "Teclea la altura:"
		Leer altura
		areaa <- (base*altura)/2
		Escribir areaa
	SiNo
		Escribir "Ingrese la medida del lado del cuadrado:"
		Leer lado
		areaa <- lado*lado
		Escribir areaa
	FinSi
	
FinAlgoritmo
