usuario_registrado = "admin"
contraseña_registrada = "Pass123"
intentos_maximos = 3

usuario = input("Usuario: ")
contraseña = input("Contraseña: ")
intentos = 1

if usuario == usuario_registrado and contraseña == contraseña_registrada:
    print("✓ Acceso concedido")
else:
    print(f"✗ Acceso denegado (Intento {intentos} de {intentos_maximos})" )

