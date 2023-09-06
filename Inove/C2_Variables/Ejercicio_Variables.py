# Ejercicio: Convertidor de monedas
# Escribir un programa que convierta una cantidad de dólares a una cantidad en euros. Para realizar la conversión, el programa debe pedir al usuario dos cosas: la cantidad de dólares y el tipo de cambio actual de dólar a euro.

# 1. Solicitamos la cantidad de dólares
cantidad_dolares = float(input("Introduce la cantidad de dólares que deseas convertir: "))

# 2. Solicitamos el tipo de cambio actual
tipo_cambio = float(input("Introduce el tipo de cambio de dólar a euro: "))

# 3. Realizamos la conversión
cantidad_euros = cantidad_dolares * tipo_cambio

# 4. Mostramos el resultado al usuario
print(f"{cantidad_dolares} dólares equivalen a {cantidad_euros} euros con el tipo de cambio dado.")