print("Automotores Carlitos")

monto = float(input("Por favor, ingrese el monto que desea gastar: "))
if monto < 1000000:
    print("Lo sentimos, no tenemos autos de ese valor.")
    
    monto = float(input("Por favor, ingrese el monto que desea gastar: "))
    if monto < 1000000:
        print("Lo sentimos, no tenemos autos de ese valor.")
        print("¡Gracias por visitar Automotores Carlitos!")
        exit()

marca = input("Por favor, ingrese la marca que está buscando (Ford o Chevrolet): ").lower()
if marca not in ["ford", "chevrolet"]:
    print("Lo sentimos, no trabajamos con esa marca.")
    
    marca = input("Por favor, ingrese la marca que está buscando (Ford o Chevrolet): ").lower()
    if marca not in ["ford", "chevrolet"]:
        print("Lo sentimos, no trabajamos con esa marca.")
        print("¡Gracias por visitar Automotores Carlitos!")
        exit()

puertas = int(input("Por favor, indique la cantidad de puertas (entre 3 y 5): "))
if puertas < 2 or puertas > 5:
    print("Los autos no tienen esa cantidad de puertas.")
    
    puertas = int(input("Por favor, indique la cantidad de puertas (entre 3 y 5): "))
    if puertas < 2 or puertas > 5:
        print("Los autos no tienen esa cantidad de puertas.")
        print("¡Gracias por visitar Automotores Carlitos!")
        exit()

if monto > 5000000 and marca == "ford" and puertas == 3:
    print("Tenemos disponible la Ford Ranger para ti.")
elif monto < 2000000 and marca == "chevrolet" and (puertas == 3 or puertas == 5):
    print("Tenemos disponible el Chevrolet Corsa para ti.")
elif monto < 4000000 and marca == "ford" and puertas == 4:
    print("Tenemos disponible la Ford Eco Sport para ti.")
elif 3000000 < monto < 6000000 and marca == "chevrolet":
    print("Tenemos disponible la Chevrolet Tracker para ti.")
else:
    print("Lo sentimos, no poseemos autos con esas características.")

print("¡Gracias por visitar Automotores Carlitos!")
exit()