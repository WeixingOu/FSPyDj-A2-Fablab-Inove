# Enunciado:

'''

Imagine que está trabajando en una empresa de comercio electrónico que vende diferentes tipos de productos. A cada cliente, se le asigna una etiqueta basada en la cantidad total de sus compras.

Las etiquetas son las siguientes:

"Bronce": Si el cliente ha gastado menos de $100.
"Plata": Si el cliente ha gastado entre $100 y $500.
"Oro": Si el cliente ha gastado entre $500 y $1000.
"Platino": Si el cliente ha gastado más de $1000.
Adicionalmente, hay eventos promocionales en los cuales los clientes pueden obtener descuentos basados en sus etiquetas:

"Bronce": 5% de descuento.
"Plata": 10% de descuento.
"Oro": 15% de descuento.
"Platino": 20% de descuento.

'''
gasto = int(input("Ingrese el total de las compras: "))

def etiquetas_cliente(gasto):
    if gasto < 100:
        return "Bronce"
    elif 100 <= gasto < 500:
        return "Plata"
    elif 500 <= gasto < 1000:
        return "Oro"
    else:
        return "Platino"

def descuento_cliente(etiqueta):
    if etiqueta == "Bronce":
        return 0.05
    elif etiqueta == "Plata":
        return 0.10
    elif etiqueta == "Oro":
        return 0.15
    else:
        return 0.20

def precio_final(gasto, etiqueta):
    return gasto * (1 - descuento_cliente(etiqueta))

print(f"El precio final con descuento para un cliente {etiquetas_cliente(gasto)} es ${precio_final(gasto, etiquetas_cliente(gasto))}")