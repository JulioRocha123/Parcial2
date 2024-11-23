Algoritmo SistemaFacturacion
	// Declaración de variables
	Dimensionar catalogo(4,3)
	Definir indice_catalogo, i, encontrado, cantidad Como Entero
	Definir opcion1, codigo, nombre, categoria, detalles Como Cadena
	Definir precio, subtotal, iva, total Como Real
	Definir indice_detalles Como Entero
	indice_catalogo <- 0
	indice_detalles <- 0
	// Inicializar catálogo
	catalogo[0,0]<-'LB001'
	catalogo[0,1]<-'Refrigerador'
	catalogo[0,2]<-'1500'
	catalogo[0,3]<-'Línea Blanca'
	catalogo[1,0]<-'PE001'
	catalogo[1,1]<-'Licuadora'
	catalogo[1,2]<-'100'
	catalogo[1,3]<-'Pequeños Electrodomésticos'
	catalogo[2,0]<-'EN001'
	catalogo[2,1]<-'Televisor'
	catalogo[2,2]<-'800'
	catalogo[2,3]<-'Entretenimiento'
	indice_catalogo <- 3
	// Menú principal
	Mientras Verdadero Hacer
		Escribir '--- Menú Principal ---'
		Escribir '1. Ver catálogo de productos'
		Escribir '2. Realizar venta'
		Escribir '3. Agregar nuevo producto'
		Escribir '4. Salir'
		Escribir 'Seleccione una opción: '
		Leer opcion
		Si opcion='1' Entonces
			// Ver catálogo
			Escribir '--- Catálogo de Productos ---'
			Para i<-0 Hasta indice_catalogo-1 Hacer
				Escribir 'Código: ', catalogo[i,0], ' | Nombre: ', catalogo[i,1], ' | Precio: $', catalogo[i,2], ' | Categoría: ', catalogo[i,3]
			FinPara
		FinSi
		Si opcion='2' Entonces
			// Realizar venta
			subtotal <- 0
			indice_detalles <- 0
		FinSi
	FinMientras
	Mientras Verdadero Hacer
		Escribir 'Ingrese el código del producto'
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
		Escribir 'Ingrese el código del producto: '
		Leer codigo
		Escribir 'Ingrese el nombre del producto: '
		Leer nombre
		Escribir 'Ingrese el precio del producto: '
		Leer precio
		Escribir 'Ingrese la categoría del producto: '
		Leer categoria
		subtotal <- subtotal+precioProducto
		Escribir 'Producto agregado exitosamente.'
	SiNo
		Si opcion='4' Entonces
			Escribir 'Gracias por usar el sistema de facturación. ¡Hasta luego!'
		SiNo
			Escribir 'Opción inválida. Intente nuevamente.'
		FinSi
	FinSi
FinAlgoritmo
