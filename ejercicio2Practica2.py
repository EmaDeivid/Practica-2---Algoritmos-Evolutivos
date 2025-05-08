import numpy as np

presupuesto = 15

precios = np.array([2.50, 3.00, 1.80]) 

max_viajes = np.floor(presupuesto/precios)

max_viajes.max()
max_viajes.argmax()
cantidad_max = int(max_viajes.max())
indice_max = int(max_viajes.argmax())

precio_min = precios.min()
indice_precio_min = int(precios.argmin())

nombres = ["Bus","Combi","Tren"]

print("Resultados")
for i, nombre in enumerate(nombres):
    print(f"Medio de Transporte {nombre}: precio $/{precios[i]:.2f} -> puede pagar {int(max_viajes[i])} viajes")

print(f"\nCon S/ {presupuesto:.2f} obtienes la mayor cantidad de viajes ({cantidad_max}) en el medio de transporte {nombres[indice_max]}.")
print(f"El precio más bajo es S/ {precio_min:.2f} del medio de transporte {nombres[indice_precio_min]}.")