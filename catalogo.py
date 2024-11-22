from factura import *
catalogo = {
    "Linea Blanca": [
        {"codigo": "LB001", "nombre": "Refrigerador", "precio": 1500},
        {"codigo": "LB002", "nombre": "Lavadora", "precio": 1200},
    ],
    "Pequeños Electrodomésticos": [
        {"codigo": "PE001", "nombre": "Licuadora", "precio": 100},
        {"codigo": "PE002", "nombre": "Cafetera", "precio": 80},
    ],
    "Entretenimiento": [
        {"codigo": "EN001", "nombre": "Televisor", "precio": 800},
        {"codigo": "EN002", "nombre": "Sistema de Sonido", "precio": 500},
    ],
    "Aires Acondicionados": [
        {"codigo": "AA001", "nombre": "Climatizador", "precio": 1200},
    ],
}

# Función para buscar un producto por su código
def buscar_producto_por_codigo(codigo, catalogo):
    for categoria, productos in catalogo.items():
        for producto in productos:
            if producto["codigo"] == codigo:
                return producto
    return None

# Función para agregar un nuevo producto al catálogo
def agregar_producto(catalogo, categoria, codigo, nombre, precio):
    if categoria in catalogo:
        catalogo[categoria].append({"codigo": codigo, "nombre": nombre, "precio": precio})
    else:
        catalogo[categoria] = [{"codigo": codigo, "nombre": nombre, "precio": precio}]
    print(f"Producto '{nombre}' agregado exitosamente a la categoría '{categoria}'.")
#-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
# Función para realizar una venta
def realizar_venta(catalogo):
    factura = Factura()
    while True:
        codigo = input("Ingrese el código del producto (o 'fin' para terminar): ")
        if codigo.lower() == "fin":
            break
        producto = buscar_producto_por_codigo(codigo, catalogo)
        if producto:
            cantidad = int(input(f"Ingrese la cantidad para {producto['nombre']}: "))
            factura.agregar_producto(producto["nombre"], cantidad, producto["precio"])
        else:
            print("Producto no encontrado.")
    
    factura.calcular_totales()
    factura.mostrar_factura()
    factura.guardar_factura()
