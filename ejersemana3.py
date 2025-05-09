productos = []


def menu():
    print("Bienvenido al sistema de gestión de productos\n 1. Agregar producto\n 2. Eliminar producto\n " 
    "3. Listar productos\n 4. Actualizar precio\n 5. Valor total del inventario\n 6. Salir del programa")

def eliminar_producto(nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado con éxito.")
            return
    print(f"El producto {nombre} no se encuentra en la lista.")

def consultar_producto(nombre):
    if not productos:
        print("No hay productos registrados.")
        return
    encontrado = False
    for producto in productos:
        if producto["nombre"] == nombre:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']:.3f}, Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print(f"El producto con nombre '{nombre}' no se encuentra en la lista.")

def actualizar_precio(nombre, nuevo_precio):
    for producto in productos:
        if producto["nombre"] == nombre:
            producto["precio"] = nuevo_precio
            print(f"El producto con el nombre {nombre} fue actualizado correctamente")
            return
    print(f"El producto {nombre} no se en la lista")

def agregar_producto(nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)
    print(f"Producto {nombre} agregado con éxito.")

calcular_total = lambda: sum(map(lambda x: x["precio"] * x["cantidad"], productos))
      
while True:
    menu()
    opcion_str = input("Ingrese la opción deseada: ").strip()#strip() elimina los espacios en blanco

    if not opcion_str.isdigit():#isdigit() verifica si es un digito
        print("Opción no válida. Por favor, elija una opción del menú.")
        continue
    
    opcion = int(opcion_str)#convertir a entero

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del producto: ").lower().strip()
            if not nombre or not nombre.isalpha():  # Verifica que el nombre solo contenga letras
                print("\033[91mEl nombre debe contener solo letras y no puede estar vacío.\033[0m")
                continue

            precio_str = input("Ingrese el precio del producto: ").strip()
            if not precio_str.replace(".", "", 1).isdigit():
                print("\033[91mEl precio debe ser un número válido.\033[0m")
                continue
            precio = float(precio_str)
            if precio < 0:
                print("\033[91mEl precio no puede ser negativo.\033[0m")
                continue

            cantidad_str = input("Ingrese la cantidad del producto: ").strip()
            if not cantidad_str.isdigit():
                print("\033[91mLa cantidad debe ser un número entero.\033[0m")
                continue
            cantidad = int(cantidad_str)
            if cantidad < 0:
                print("\033[91mLa cantidad no puede ser negativa.\033[0m")
                continue
            agregar_producto(nombre, precio, cantidad)
              
        case 2:
            nombre = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
            if not nombre or not nombre.isalpha():
                print("El nombre solo debe contener letras y no puede estar vacío.")
                continue
            eliminar_producto(nombre)
        case 3:
                nombre = input("Ingrese el nombre del producto que desea consultar: ").strip().lower()
                consultar_producto(nombre)
        case 4:
                nombre = input("Ingrese el nombre del producto a actualizar: ").strip().lower()
                if not nombre or not nombre.isalpha():
                    print("El nombre solo debe contener letras y no puede estar vacío.")
                    continue

                nuevo_precio_str = input("Ingrese el nuevo precio del producto: ").strip().lower()
                if not nuevo_precio_str.replace(".", "", 1).isdigit():
                    print("El precio debe ser un número válido.")
                    continue
                nuevo_precio = float(nuevo_precio_str)
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                actualizar_precio(nombre, nuevo_precio)

        case 5:
            total = calcular_total()
            print(f"| El valor total del inventario es: | ${total:,.3f} |")
        case 6:
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Por favor, elija una opción del menú.")

