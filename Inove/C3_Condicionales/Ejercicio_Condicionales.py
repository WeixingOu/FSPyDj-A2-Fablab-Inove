# Ejercicio: Categorización de películas
# Descripción:
# Supongamos que trabajas en una tienda de películas y te piden clasificar las películas basadas en su edad recomendada y género.

# Si la película es para todos los públicos y es de animación, debe ser categorizada como "Familiar".
# Si es solo para adultos y es un drama, debe ser categorizada como "Drama para adultos".
# Si es de acción y es para mayores de 16, categorízala como "Acción para jóvenes".
# Para todas las demás combinaciones, categorízala como "General".

# 1. Solicitamos el género de la película
genero = input("Introduce el género de la película (animación, drama, acción, etc.): ").strip().lower()

# 2. Solicitamos la edad recomendada
edad = int(input("Introduce la edad recomendada de la película (todos los públicos, mayores de 16, solo para adultos): "))

# 3. Usamos condicionales para determinar la categoría
if genero == "animación" and edad:
    categoria = "Familiar"
elif genero == "drama" and edad >= 16:
    categoria = "Drama para adultos"
elif genero == "acción" and edad < 16:
    categoria = "Acción para jóvenes"
else:
    categoria = "General"

# 4. Mostramos la categoría al usuario
print(f"La película se categoriza como: {categoria}")