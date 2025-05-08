import pandas as pd

datos = {
'Gastos_dia': [4.0, 3.5, 5.0, 4.2, 3.8],
'Dias': ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

}

df = pd.DataFrame(datos)
stats = df['Gastos_dia'].describe()

gasto_medio = stats['mean']
gasto_total = df['Gastos_dia'].sum()

df_mayor_medio = df[df['Gastos_dia'] > gasto_medio]

lista_altos = df_mayor_medio['Dias'].tolist()


print(f"\nEl gasto total es: {gasto_total:.2f}.")
print(f"\nEl gasto medio es: {gasto_medio:.2f}.")

print("Dias que gastó más que el promedio:")
for dias in lista_altos:
    print(f" - {dias}")


