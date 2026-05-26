# ==========================================
# Evaluación Final - Fundamentos de Programación
# Problema 5
# ==========================================

# Matriz con recursos y horas trabajadas
recursos = [
    ["Ana", 8, 8, 9, 8, 8],
    ["Carlos", 10, 9, 8, 9, 10],
    ["Laura", 7, 8, 7, 8, 7],
    ["Miguel", 9, 9, 9, 9, 9]
]

# Función para calcular el total de horas
def calcular_total_horas(fila):

    total = sum(fila[1:])

    return total

# Función para clasificar la jornada
def clasificar_jornada(total_horas):

    if total_horas > 40:
        return "Sobretiempo"

    else:
        return "Horario Estándar"

# Mostrar resultados
print("===== REPORTE DE HORAS TRABAJADAS =====")

for recurso in recursos:

    nombre = recurso[0]

    total = calcular_total_horas(recurso)

    clasificacion = clasificar_jornada(total)

    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------------")