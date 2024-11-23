Algoritmo SistemaFacturacion
	// Declaraci�n de variables
	Dimensionar catalogo(4,3)
	Definir indice_catalogo, i, encontrado, cantidad Como Entero
	Definir opcion1, codigo, nombre, categoria, detalles Como Cadena
	Definir precio, subtotal, iva, total Como Real
	Definir indice_detalles Como Entero
	indice_catalogo <- 0
	indice_detalles <- 0
	// Inicializar cat�logo
	catalogo[0,0]<-'LB001'
	catalogo[0,1]<-'Refrigerador'
	catalogo[0,2]<-'1500'
	catalogo[0,3]<-'L�nea Blanca'
	catalogo[1,0]<-'PE001'
	catalogo[1,1]<-'Licuadora'
	catalogo[1,2]<-'100'
	catalogo[1,3]<-'Peque�os Electrodom�sticos'
	catalogo[2,0]<-'EN001'
	catalogo[2,1]<-'Televisor'
	catalogo[2,2]<-'800'
	catalogo[2,3]<-'Entretenimiento'
	indice_catalogo <- 3
	// Men� principal
	Mientras Verdadero Hacer
		Escribir '--- Men� Principal ---'
		Escribir '1. Ver cat�logo de productos'
		Escribir '2. Realizar venta'
		Escribir '3. Agregar nuevo producto'
		Escribir '4. Salir'
		Escribir 'Seleccione una opci�n: '
		Leer opcion
		Si opcion='1' Entonces
			// Ver cat�logo
			Escribir '--- Cat�logo de Productos ---'
			Para i<-0 Hasta indice_catalogo-1 Hacer
				Escribir 'C�digo: ', catalogo[i,0], ' | Nombre: ', catalogo[i,1], ' | Precio: $', catalogo[i,2], ' | Categor�a: ', catalogo[i,3]
			FinPara
		FinSi
		Si opcion='2' Entonces
			// Realizar venta
			subtotal <- 0
			indice_detalles <- 0
		FinSi
	FinMientras
	Mientras Verdadero Hacer
		Escribir 'Ingrese el c�digo del producto'
		Leer codigo
		Si codigo='fin' Entonces
		
		FinSi
		encontrado <- -1
		Para i<-0 Hasta indice_catalogo-1 Hacer
			Si catalogo[i,0]=codigo Entonces
				encontrado <- i
			FinSi
		FinPara
	FinMientras
	// Calcular totales
	iva <- subtotal*0.19
	total <- subtotal+iva
	// Mostrar factura
	Escribir '--- Factura ---'
	Escribir 'Subtotal: $', subtotal
	Escribir 'IVA (19%): $', iva
	Escribir 'Total: $', total
	Si opcion='3' Entonces
		// Agregar nuevo producto
		Escribir 'Ingrese el c�digo del producto: '
		Leer codigo
		Escribir 'Ingrese el nombre del producto: '
		Leer nombre
		Escribir 'Ingrese el precio del producto: '
		Leer precio
		Escribir 'Ingrese la categor�a del producto: '
		Leer categoria
		subtotal <- subtotal+precioProducto
		Escribir 'Producto agregado exitosamente.'
	SiNo
		Si opcion='4' Entonces
			Escribir 'Gracias por usar el sistema de facturaci�n. �Hasta luego!'
		SiNo
			Escribir 'Opci�n inv�lida. Intente nuevamente.'
		FinSi
	FinSi
FinAlgoritmo
