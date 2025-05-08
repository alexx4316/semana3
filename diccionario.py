agenda = {}

def listar_contactos(agenda):
    if not agenda:
        print("No hay contactos registrados.")
    else:
        print("Lista de contactos registrados:")
        #. items recorre el diccionario y devuelve una lista de tuplas (clave, valor)
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Telefono: {telefono}")
def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        print(f"Nombre: {nombre}, Telefono: {agenda[nombre]}")
    else:
        print("El contacto no se encuentra en la agenda.")
def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Se ha eliminado el contacto {nombre}.")
    else:
        print("El contacto no se encuentra en la agenda.")

while True:
    print("Bienvenido a la agenda de contactos")
    print("1. Registrar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Listar contactos")
    print("5. Salir del programa")

    opcion = input("Ingrese la opción deseada: ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el telefono del contacto: ")
            agenda[nombre] = telefono
        case "2":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(agenda, nombre)
        case "3":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(agenda, nombre)
        case "4":
            listar_contactos(agenda)
        case "5":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Por favor, elija una opción del menú.")