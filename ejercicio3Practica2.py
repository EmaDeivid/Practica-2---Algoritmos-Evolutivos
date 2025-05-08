
import pandas as pd

datos = {
'Estudiante': ['Rosa', 'David', 'Elena', 'Mario', 'Paula'],
'Dias_prestamo': [7, 10, 5, 12, 3]
}

df = pd.DataFrame(datos)
stats = df['Dias_prestamo'].describe()

df_mayor_8 = df[df['Dias_prestamo'] > 8.0]

uso_promedio = stats['mean']
lista_altos = df_mayor_8['Estudiante'].tolist()


print(f"\nEl uso promedio por estudiante {uso_promedio:.2f}.")
print("Estudiantes que usaron por más de 8 días:")
for alumno in lista_altos:
    print(f" - {alumno}")