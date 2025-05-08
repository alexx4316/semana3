productos = []


def menu():
    print("Bienvenido al sistema de gestión de productos\n 1. Agregar producto\n 2. Eliminar producto\n " \
    "3. Listar productos\n 4. Actualizar precio\n 5. Salir del programa")

def eliminar_producto(nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado con éxito.")
            return
    print(f"El producto{nombre} no se encuentra en la lista.")
def consultar_producto():
    if not productos:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    # busca por nombre especifico
    # for producto in productos:
    #     if producto["nombre"] == nombre:
    #         print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    #         encontrado = True
    #         break   
     
def actualizar_precio(nombre, nuevo_precio):
    for producto in productos:
        if producto["nombre"] == nombre:
            producto["precio"] = nuevo_precio
def calcular_total():
    total = 0
    for producto in productos:
        total += producto["precio"] * producto["cantidad"]
    return total

def agregar_producto(nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)
    print(f"Producto {nombre} agregado con éxito.")

while True:
    menu()
    opcion_str = input("Ingrese la opción deseada: ").strip()#strip() elimina los espacios en blanco
    opcion = int(opcion_str)#convertir a entero
    if not opcion_str.isdigit():#isdigit() verifica si es un digito
        print("Opción no válida. Por favor, elija una opción del menú.")
        continue

    match opcion:
        case 1:
            try:
                nombre = input("Ingrese el nombre del producto: ").lower().strip()
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                if not nombre.isalpha():  # Verifica que el nombre solo contenga letras
                    raise ValueError(f"\033[91mEl nombre no puede contener números o caracteres especiales.\033[0m")
                
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    raise ValueError("El precio no puede ser negativo.")

                cantidad = int(input("Ingrese la cantidad del producto: "))
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
                agregar_producto(nombre, precio, cantidad)
            except ValueError as e:
                print(f"\033[91m Error: {e}. Intenta de nuevo.\033[0m\n")
                #raise se usa para lanzar una excepcion de manera intencionada, es decir detiene la ejecucion y muestra el error pero con el except vuelve y pide el dato
        case 2:
            try:
                nombre = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
                if not nombre:
                    raise ValueError("El nombre solo debe contener letras.")
                eliminar_producto(nombre)
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")
        case 3:
                consultar_producto()
        case 4:
            try:
                nombre = input("Ingrese el nombre del producto a actualizar: ").strip().lower()
                if not nombre:
                    raise ValueError("El nombre solo debe contener letras.")
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                if nuevo_precio < 0:
                    raise ValueError("El precio no puede ser negativo.")
                actualizar_precio(nombre, nuevo_precio)
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")
        case 5:
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Por favor, elija una opción del menú.")

