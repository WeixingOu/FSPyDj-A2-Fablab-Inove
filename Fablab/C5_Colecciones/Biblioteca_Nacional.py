import random

print("\nBienvenido al sistema de gestión online de la biblioteca Nacional")

infantiles = ['Blancanieves', 'Los Tres Chanchitos', 'Cenicienta']
novelas = ['Don Quijote', 'La Novicia Revelde']
policiales = ['Sherlok Holmes', 'Muerte en el Nilo']

stock = {titulo: random.randint(1, 10) for titulo in infantiles + novelas + policiales}

def main():
    print("\nSeleccione una tarea: \n 1. Ver libros disponibles \n 2. Eliminar libros \n 3. Agregar libros \n 4. Ver el stock de libros \n 5. Salir del sistema")
    opcion = input()

    if opcion == "1":
        ver_libros()
    elif opcion == "2":
        eliminar_libro()
    elif opcion == "3":
        agregar_libro()
    elif opcion == "4":
        ver_stock()
    elif opcion == "5":
        print("Gracias por usar el sistema de gestión online de la biblioteca Nacional.")
        exit()
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
        main()
    
def ver_libros():
    print("\nSeleccione una categoría: \n 1. Infantiles \n 2. Novelas \n 3. Policiales \n 4. Ver todas")
    opcion = input()
    
    if opcion == "1":
        print("Infantiles:", infantiles)
        main()
    elif opcion == "2":
        print("Novelas:", novelas)
        main()
    elif opcion == "3":
        print("Policiales:", policiales)
        main()
    elif opcion == "4":
        print("Infantiles:", infantiles)
        print("Novelas:", novelas)
        print("Policiales:", policiales)
        main()
    else:
        print("Opción no válida.")
        main()

def eliminar_libro():
    titulo = input("Ingrese el título del libro a borrar: ").capitalize()
    
    if titulo in stock:
        stock.pop(titulo)
        if titulo in infantiles:
            infantiles.remove(titulo)
        elif titulo in novelas:
            novelas.remove(titulo)
        elif titulo in policiales:
            policiales.remove(titulo)
        print(f"El libro {titulo} ha sido eliminado.")
        main()
    else:
        print("El libro no existe en nuestro sistema.")
        main()

def agregar_libro():
    print("\nSeleccione una categoría: \n 1. Infantiles \n 2. Novelas \n 3. Policiales")
    
    opcion = input()
    titulo = input("Ingrese el título del libro a agregar: ").capitalize()

    if opcion == "1":
        infantiles.append(titulo)
        stock[titulo] = random.randint(1, 10)
        main()
    elif opcion == "2":
        novelas.append(titulo)
        stock[titulo] = random.randint(1, 10)
        main()
    elif opcion == "3":
        policiales.append(titulo)
        stock[titulo] = random.randint(1, 10)
        main()
    else:
        print("Categoría no válida.")
        main()

def ver_stock():
    titulo = input("Ingrese el título del libro para verificar el stock: ").capitalize()

    if titulo in stock:
        print(f"El stock del libro {titulo} es: {stock[titulo]} ejemplares.")
        main()
    else:
        print("El libro no existe en nuestro sistema.")
        main()
main()