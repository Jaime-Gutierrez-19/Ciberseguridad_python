import random

# 1. Definimos los "ingredientes" de la contraseña
letras = "abcdefghijklmnopqrstuvwxyz"
letras_mayus = letras.upper() # Truco para tener mayúsculas rápido
numeros = "0123456789"
simbolos = "!@#$%^&*"

# Unimos todo en una sola "bolsa" de caracteres posibles
caracteres_totales = letras + letras_mayus + numeros + simbolos

# 2. Pedimos al usuario la longitud (Input)
print("=== GENERADOR DE PASSWORD ROBUSTO ===")
try:
    longitud = int(input("¿De cuántos caracteres quieres tu contraseña? (Ej. 12): "))
except ValueError:
    print("Error: Por favor ingresa un número válido.")
    exit()

# 3. Generamos la contraseña (Lógica)
password_generada = ""

# Usamos un bucle para elegir un caracter al azar 'n' veces
for i in range(longitud):
    caracter_aleatorio = random.choice(caracteres_totales)
    password_generada += caracter_aleatorio

# 4. Mostramos el resultado (Output)
print(f"\n🔐 Tu nueva contraseña es: {password_generada}")
