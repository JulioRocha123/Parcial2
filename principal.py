from catalogo import catalogo, agregar_producto
from ventas import realizar_venta, contador_ventas

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver catálogo de productos")
        print("2. Realizar venta")
        print("3. Agregar nuevo producto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Catálogo de Productos ---")
            for categoria, productos in catalogo.items():
                print(f"\n{categoria}")
                for producto in productos:
                    print(f"- {producto['nombre']} (Código: {producto['codigo']}, Precio: {producto['precio']})")
        elif opcion == "2":
            realizar_venta(catalogo)
        elif opcion == "3":
            print("\n--- Agregar Nuevo Producto ---")
            categoria = input("Ingrese la categoría del producto: ").title()
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            agregar_producto(catalogo, categoria, codigo, nombre, precio)
        elif opcion == "4":
            print("Gracias por usar el sistema de facturación. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()