# =================== EJERCICIO 1 =======================
"""
Calculando los años de recuperación
"""

# Definiendo las variables
CantidadInvertida = 1000
IngresosAnuales = 100

AnosRecuperacion = CantidadInvertida/IngresosAnuales

# Total
print(AnosRecuperacion)


# =================== EJERCICIO 2 =======================
"""
Calculando los ingresos anuales requeridos
"""

# Definiendo las variables
CantidadInvertida = 1000
AnosRecuperacion = 5

IngresosAnuales = CantidadInvertida/AnosRecuperacion

# Total
print(IngresosAnuales)


# =================== EJERCICIO 3 =======================
"""
Calculando los ingresos anuales requeridos
Valores modificados
"""

# Definiendo las variables
CantidadInvertida = 2500
AnosRecuperacion = 3

IngresosAnuales = CantidadInvertida/AnosRecuperacion

# Total
print(IngresosAnuales)


# =================== EJERCICIO 4 =======================
"""
Variables que almacenan cadenas
"""

# Definiendo las variables
Hola = "hola"

HolaPor5 = Hola * 5

# Visualizar variable
print(HolaPor5)


## =================== EJERCICIO 5 =======================
"""
Variables que almacenan arreglos
"""

lista = [1, 4, 5]
type(lista)

tupla = (1, 5, 4)
type(tupla)


## =================== EJERCICIO 6 =======================
"""
Manipulando listas
"""

# definiendo una lista
lista = ["objeto 1", "objeto 2", "objeto 3", "objeto 4"]

# recuperar el objeto 2, recordar que listas empiezan en 0
lista[1]

# eliminar el último elemento de la lista
lista.pop()

# eliminar un elemento determinado de la lista
lista.pop(2)

# modificar un elemento de la lista
lista[2] = "nuevo objeto 3"

# agregar un elemento al final de la lista
lista.append("objeto 5")



## =================== EJERCICIO 7 =======================
"""
Valores lógicos
"""

# ejemplos usando "Y"

# los siguientes comandos producirán True
Proposicion1 = (2 + 2) == 4
Proposicion2 = True

# evaluación
Proposicion1 and Proposicion2

# esta sentencia producirá False
Proposicion1 = 3 < 1
Proposicion2 = 3 > 1

# evaluación
Proposicion1 and Proposicion2


# ejemplos usando "O"

# los siguientes comandos producirán True
Proposicion1 = 3**2 == 9
Proposicion2 = 2 + 2 == "pez"

# evaluación
Proposicion1 or Proposicion2

# los siguientes comandos producirán True
Proposicion1 = "Hola" == "hola"
Proposicion2 = "Adiós" == "adiós"

# evaluación
Proposicion1 or Proposicion2

# Ejemplos usando negación
# entendiendo la lógica
not True
not False

# negar uno de los ejemplos anteriores

# los siguientes comandos producirán True
Proposicion1 = (2 + 2) == 4
Proposicion2 = True

# evaluación
not Proposicion1 and Proposicion2

# booleanos como números
True == 1
False == 0
True + True + True