# Definir las ganancias y las restricciones
ganancia_max = 0
mejor_x = 0
mejor_y = 0

# Probar combinaciones de A (x) y B (y)
for x in range(10, 61):  # x ≥ 10, probamos hasta 60 unidades (por ejemplo)
    for y in range(5, 41):  # y ≥ 5, probamos hasta 40 unidades (por ejemplo)
        # Verificar que las restricciones se cumplen
        if 2 * x + 3 * y <= 120:  # Restricción de horas
            ganancia = 50 * x + 80 * y  # Función objetivo
            if ganancia > ganancia_max:  # Maximizar la ganancia
                ganancia_max = ganancia
                mejor_x = x
                mejor_y = y

# Mostrar resultados
print(f"Unidades de A: {mejor_x}")
print(f"Unidades de B: {mejor_y}")
print(f"Ganancia máxima: ${ganancia_max}")
