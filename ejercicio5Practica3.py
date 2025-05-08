import numpy as np

paquetes = np.array([1, 2, 5,10]) 
precios = np.array([5, 9, 20, 35])

costo_paquete = precios/paquetes

print("Costo por paquete: ")
for i in range(len(paquetes)):
    print(f"  - {paquetes[i]} GB por S/ {precios[i]}: $/ {costo_paquete[i]:.2f} por GB")


min = np.argmin(costo_paquete)
print("El paquete más económico por GB es el de", paquetes[min], "GB a $/", precios[min])