import datetime
class Factura:
    def __init__(self):
        self.detalles = []  # Lista para guardar los productos comprados
        self.subtotal = 0
        self.iva = 0
        self.total = 0

    def agregar_producto(self, nombre, cantidad, precio):
        subtotal_producto = cantidad * precio
        self.detalles.append({"nombre": nombre, "cantidad": cantidad, "precio": precio, "subtotal": subtotal_producto})
        self.subtotal += subtotal_producto

    def calcular_totales(self):
        self.iva = self.subtotal * 0.19
        self.total = self.subtotal + self.iva

    def mostrar_factura(self):
        print("\n----- Factura -----")
        for detalle in self.detalles:
            print(f"{detalle['nombre']} x{detalle['cantidad']} @ {detalle['precio']} = {detalle['subtotal']}")
        print(f"Subtotal: {self.subtotal}")
        print(f"IVA (19%): {self.iva}")
        print(f"Total: {self.total}")

    def guardar_factura(self):
        # Generar un nombre único para la factura usando la fecha y hora actual
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        archivo = f"factura_{timestamp}.txt"
        with open(archivo, "w") as f:
            f.write("----- Factura -----\n")
            for detalle in self.detalles:
                f.write(f"{detalle['nombre']} x{detalle['cantidad']} @ {detalle['precio']} = {detalle['subtotal']}\n")
            f.write(f"Subtotal: {self.subtotal}\n")
            f.write(f"IVA (19%): {self.iva}\n")
            f.write(f"Total: {self.total}\n")
        print(f"Factura guardada en el archivo '{archivo}'.")