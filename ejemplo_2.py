# Herramienta de reporte de incidentes
print("\n=== GENERADOR DE REPORTE DE INCIDENTES ===\n")

tipo_incidente = input("Tipo de incidente (virus/phishing/acceso): ")
fecha = input("Fecha del incidente (DD/MM/YYYY): ")
descripción = input("Descripción breve: ")
severidad = input("Severidad (Baja/Media/Alta/Crítica): ")

print("\n=== REPORTE GENERADO ===")
print(f"Tipo: {tipo_incidente}")
print(f"Fecha: {fecha}")
print(f"Descripción: {descripción}")
print(f"Severidad: {severidad}")
