print("Supermercados La Ilusión")

nombre = input("Por favor, ingrese su nombre: ")

gastoVerduderia = float(input(f"{nombre}, por favor indique el monto que gastó en verdulería: "))
gastoCarniceria = float(input("Indique el monto que gastó en en carnicería: "))
gastoOtros = float(input("Indique el monto que gastó en otros sectores: "))

print(f"{nombre}, el costo total de su compra es: ${(gastoVerduderia + gastoCarniceria + gastoOtros):.2f}")

print(f"{nombre} tienes un descuento del 10%. Tu monto final con el beneficio es: ${((gastoVerduderia + gastoCarniceria + gastoOtros) - ((gastoVerduderia + gastoCarniceria + gastoOtros) * 0.10)):.2f}")

print("Gracias por usar nuestro sistema.")