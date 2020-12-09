Algoritmo TipoDeTriangulo
	definir lado1, lado2, lado3 Como entero
	Escribir "ingrese el lado 1 del triangulo"
	Leer lado1
	Escribir "ingrese el lado 2 del triangulo"
	Leer lado2
	Escribir "ingrese el lado 3 del triangulo"
	Leer lado3
	Si lado1 = lado2 y lado2 = lado3 y lado3 = lado1 Entonces
		Escribir "tu triangulo es equilatero"
	SiNo si lado1=lado2 o lado2=lado3 o lado3=lado1 entonces
			Escribir "tu triangulo es iscoceles"
		SiNo
			Escribir "Tu triangulo es escaleno"
		FinSi
	FinSi
	
	
FinAlgoritmo
