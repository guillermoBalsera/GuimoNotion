
# Lectura de ficheros

## Leer todo el contenido del fichero como una cadena de texto

```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

## Leer un archivo linea a linea

```python
with open("archivo.txt", "r") as archivo:
    linea = archivo.readline()
    while linea:
        print(linea, end="")
        linea = archivo.readline()
```

## Obtener una lista con las lineas del archivo

```python
with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea, end="")
```

```python
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea, end="")
```

## Lectura de archivos binarios

```python
with open("archivo.bin", "rb") as archivo_binario:
    datos = archivo_binario.read()
```

## Lectura de ficheros CSV

### Leer el archivo CSV linea a linea

```python
import csv

with open("datos.csv", newline="") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    for fila in lector_csv:
        print(fila)
```

### Almacenarlo en un diccionario

```python
import csv

datos_diccionario = []

with open("datos.csv", newline="") as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)

    for fila in lector_csv:
        datos_diccionario.append(fila)
```

### Almacenarlo en una coleccion de objetos

```python
import csv

personas = []

with open("datos.csv", newline="") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    for fila in lector_csv:
        nombre, edad, ciudad = fila
        persona = Persona(nombre, edad, ciudad)
        personas.append(persona)
```

## Pickle

```python
import pickle

with open("objetos.pkl", "rb") as archivo:
    personas_recuperadas = pickle.load(archivo)

for persona in personas_recuperadas:
    print(persona.nombre, persona.edad)
```