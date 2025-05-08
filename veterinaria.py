nombres = []
edades = []
enfermos = []
 
def registrar_mascota():
        nombre = input("Ingresa el nombre de la mascota: ")
        nombres.append(nombre)
        edad = input("Ingresa la edad de la mascota: ")
        edades.append(edad)
        enfermo = input("¿La mascota esta enferma? (si/no): ")
        enfermos.append(enfermo)

def eliminar_mascota(nombre):
    if nombre in nombres:
        index = nombres.index(nombre)
        del nombres[index]
        del edades[index]
        del enfermos[index]
        print(f"Se ha eliminado la mascota {nombre}.")
    else:
        print("La mascota no se encuentra en el registro.")
def listar_mascotas():
    if not nombres:
        print("No hay mascotas registradas.")
    else:
        print("Lista de mascotas registradas:")
        for i in range(len(nombres)):
            print(f"{i+1},Nombre: {nombres[i]}, Edad: {edades[i]}, Enfermo: {enfermos[i]}")

def mostrar_menu():
    print("Bienvenido al registro de mascotas")
    print("1. Registrar mascota")
    print("2. Eliminar mascota")
    print("3. Listar mascotas")
    print("4. Salir del programa")
def main():
    hacerOtraCosa = True

    while hacerOtraCosa:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        match opcion:
            case "1":
                registrar_mascota()
            case "2":
                eliminar_mascota(nombre=input("Ingrese el nombre de la mascota a eliminar: "))
            case "3":
                listar_mascotas()
            case _:
                print("Opción no válida. Por favor, elija una opción del menú.")

    respuesta = input("¿Quieres hacer algo más? (sí/no): ").strip().lower()
    if hacerOtraCosa:
        if respuesta == "no":
            hacerOtraCosa= False
            print("Saliendo del programa.")
main()
