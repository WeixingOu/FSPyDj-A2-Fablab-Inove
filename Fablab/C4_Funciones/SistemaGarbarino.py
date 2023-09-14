nombre = input("Por favor, ingrese su nombre: ")

print(f"¡Bienvenido al sistema de Garbarino! {nombre}!")

opcion = input("\nSeleccione una opcion: \n 1. Comprar electrodomesticos \n 2. Comprar musica \n 3. Ambos \n")

def comprar_electrodomesticos():
    print("\nElectrodomesticos disponibles: \n 1. Heladera - $50000 \n 2. TV - $35000 \n 3. Licuadora - $5000")
    opcion = input("¿Que desea comprar? ")
    
    if opcion == "1":
        return 500
    elif opcion == "2":
        return 300
    elif opcion == "3":
        return 450
    else:
        print("Opcion no valida.")
        return 0
    
def comprar_musica():
    
    print("\nDiscos disponibles: \n 1. Queen - $500 \n 2. Muse - $300 \n 3. The Beatles - $450")
    opcion = input("¿Que desea comprar? ")
    
    if opcion == "1":
        return 500
    elif opcion == "2":
        return 300
    elif opcion == "3":
        return 450
    else:
        print("Opcion no valida.")
        return 0

total = 0
if opcion == "1":
    total += comprar_electrodomesticos()
elif opcion == "2":
    total += comprar_musica()
elif opcion == "3":
    total += comprar_electrodomesticos()
    total += comprar_musica()
else:
    print("Opción no válida.")
    exit()

print(f"\nEl costo total de su compra es: ${total}")
print("¡Gracias por su compra en Garbarino! ¡Hasta luego!")