# ENCRIPTADOR CÉSAR v1.0

def encriptar(mensaje, clave):
    cifrado = ""
    for letra in mensaje:
        if letra.isalpha(): # Solo si es letra
            # 1. Convertir letra a numero ASCII
            numero = ord(letra)
            # 2. Sumar la clave (desplazamiento)
            numero_cifrado = numero + clave
            # 3. Convertir numero a letra de nuevo
            cifrado += chr(numero_cifrado)
        else:
            # Si es espacio o simbolo, dejar igual
            cifrado += letra
    return cifrado

# INTERFAZ DE USUARIO
print("🔐 --- SISTEMA DE ENCRIPTACIÓN --- 🔐")
texto = input("Introduce el mensaje secreto: ")
saltos = int(input("Introduce nivel de seguridad (número): "))

resultado = encriptar(texto, saltos)
print(f"\nMENSAJE PROTEGIDO: {resultado}")
