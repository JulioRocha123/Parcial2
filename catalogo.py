from factura import *
contador_ventas = 0
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
