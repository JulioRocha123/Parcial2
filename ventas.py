from factura import Factura
from catalogo import buscar_producto_por_codigo

# Contador global de ventas
contador_ventas = 0

# Función para realizar una venta
def realizar_venta(catalogo):
    global contador_ventas
    factura = Factura()
    while True:
        codigo = input("Ingrese el código del producto (o 'fin' para terminar): ")
        if codigo.lower() == "fin":
            break
        producto = buscar_producto_por_codigo(codigo, catalogo)
        if producto:
            try:
                cantidad = int(input(f"Ingrese la cantidad para {producto['nombre']}: "))
                if cantidad > 0:
                    factura.agregar_producto(producto["nombre"], cantidad, producto["precio"])
                else:
                    print("La cantidad debe ser mayor a 0.")
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad.")
        else:
            print("Producto no encontrado.")
    
    factura.calcular_totales()
    factura.mostrar_factura()
    factura.guardar_factura()
    
    contador_ventas += 1
    print(f"Venta completada. Total de ventas realizadas: {contador_ventas}")