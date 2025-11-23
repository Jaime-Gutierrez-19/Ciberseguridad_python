contraseña_correcta = "AdminPass123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    contraseña = input("Contraseña: ")
    intentos += 1
    
    if contraseña == contraseña_correcta:
        print("✓ Acceso concedido")
        break
    else:
        print(f"✗ Intento {intentos} fallido")

if intentos == max_intentos:
    print("🚨 CUENTA BLOQUEADA - Máximo de intentos superado")
