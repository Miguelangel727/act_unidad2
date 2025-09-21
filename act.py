class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []
        print(f"Inventario de la tienda '{self.nombre_tienda}' creado.")

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("Error: El precio y la cantidad deben ser valores positivos.")
            return

        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                producto["cantidad"] += cantidad
                print(f"Se actualizó el stock de '{nombre}'. Nueva cantidad: {producto['cantidad']}")
                return

        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado al inventario.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad <= 0:
                    print("Error: La cantidad a vender debe ser un valor positivo.")
                    return
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"Venta exitosa. Se vendieron {cantidad} unidades de '{nombre}'.")
                    if producto["cantidad"] == 0:
                        self.productos.remove(producto)
                        print(f"'{nombre}' se ha agotado y ha sido eliminado del inventario.")
                    return
                else:
                    print(f"Error: No hay suficiente stock. Solo quedan {producto['cantidad']} unidades de '{nombre}'.")
                    return
        print(f"Error: El producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print(f"\n--- Inventario de '{self.nombre_tienda}' ---")
        for producto in self.productos:
            print(f"{producto['nombre']}: ${producto['precio']} | Cantidad: {producto['cantidad']}")

    def producto_mas_caro(self):
        if not self.productos:
            return None, None

        mas_caro = max(self.productos, key=lambda p: p["precio"])
        return mas_caro["nombre"], mas_caro["precio"]

def main():
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    mi_tienda = InventarioTienda(nombre_tienda)

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar un producto")
        print("2. Vender un producto")
        print("3. Ver el inventario")
        print("4. Consultar el producto más caro")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                mi_tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Error: El precio debe ser un número y la cantidad un número entero.")

        elif opcion == '2':
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
                mi_tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")

        elif opcion == '3':
            mi_tienda.mostrar_inventario()

        elif opcion == '4':
            nombre_caro, precio_caro = mi_tienda.producto_mas_caro()
            if nombre_caro:
                print(f"\nEl producto más caro es '{nombre_caro}' con un precio de ${precio_caro}.")
            else:
                print("No hay productos en el inventario.")

        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")

if __name__ == "__main__":
    main()