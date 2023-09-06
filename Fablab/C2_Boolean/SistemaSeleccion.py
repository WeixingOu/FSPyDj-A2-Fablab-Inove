print("Sistema de selección de deporte")

genero = input("Por favor, indique su género: ").lower()

edad = int(input("Por favor, indique su edad: "))

altura = float(input("Por favor, indique su altura: "))

print("Mayor: " + str(edad >= 18))

print("Alto: " + str(altura > 1.8))

if genero in ["hombre", "masculino", "varón"]:
    print(f"Hombre: True")
    print(f"Puede jugar rugby: True")
    if altura > 1.8:
        print(f"Puede jugar basket: True")
    else:
        print(f"Puede jugar basket: False")
    print(f"Puede jugar fútbol: {edad < 50}")
else:
    print(f"Hombre: False")
    if altura > 1.8:
        print(f"Puede jugar volley: True")
    else:
        print(f"Puede jugar volley: False")