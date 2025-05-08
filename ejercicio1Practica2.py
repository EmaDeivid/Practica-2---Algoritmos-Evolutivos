import numpy as np

presupuesto = 8

precios = np.array([0.10, 0.12, 0.08]) 

max_copias = np.floor(presupuesto/precios)

max_copias.max()
max_copias.argmax()
cantidad_max = int(max_copias.max())
indice_max = int(max_copias.argmax())

precio_min = precios.min()
indice_precio_min = int(precios.argmin())

nombres = ['A','B','C']

print("Resultados")
for i, nombre in enumerate(nombres):
    print(f"Fotocopiadora {nombre}: precio $/{precios[i]:.2f} -> puede comprar {int(max_copias[i])} copias")

print(f"\nCon S/ {presupuesto:.2f} obtienes la mayor cantidad de copias ({cantidad_max}) en la fotocopiadora {nombres[indice_max]}.")
print(f"El precio más bajo es S/ {precio_min:.2f} en la fotocopiadora {nombres[indice_precio_min]}.")