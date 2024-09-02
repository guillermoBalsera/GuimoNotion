# Escritura de ficheros

## Escribir en un archivo de texto

```python
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.write("Este es un archivo de texto generado por python.\n")
    archivo.write("Adiós, mundo!")
```

## Agregar contenido a un archivo existente

```python
with open("archivo.txt", "a") as archivo:
    archivo.write("\n¡Esto se añade al final del archivo!")
```

## Escribir en un archivo CSV

```python
import csv

datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Juan", 30, "Ciudad de México"],
    ["María", 25, "Guadalajara"],
    ["Pedro", 40, "Monterrey"]
]

with open("datos.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    for fila in datos:
        escritor_csv.writerow(fila)
```

## Pickle

```python
import pickle

personas = [juan, maria, pedro]

with open("objetos.pkl", "wb") as archivo:
    pickle.dump(personas, archivo)
```