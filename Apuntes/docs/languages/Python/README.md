## Funcionalidades básicas

### Print

```python
print("Hola mundo")
```

```python
print("Primera línea\nSegunda línea\nTercera línea")
```

```python
print("Primera línea", end=" ")
print("Segunda línea", end=" ")
print("Tercera línea")
```

### Input

```python
nombre = input("¿Cuál es tu nombre? ")
```

### Longitud

```python
mi_lista = [1, 2, 3, 4, 5]
print(len(mi_lista))  # Output: 5
```

### Type

```python
print(type(123))          # Output: <class 'int'>
print(type(3.14))         # Output: <class 'float'>
print(type("Hola"))       # Output: <class 'str'>
print(type([1, 2, 3]))    # Output: <class 'list'>
```

### Conversión de tipos

```python
print(int("123"))       # Output: 123
print(float("3.14"))    # Output: 3.14
print(str(123))         # Output: '123'
print(list("Hola"))     # Output: ['H', 'o', 'l', 'a']
```

### Range

La función range() se utiliza para generar una secuencia de números. Comúnmente se usa en bucles for.

```python
range(inicio, fin, paso)
```

> NOTE
> inicio: El valor inicial de la secuencia (por defecto es 0).
> fin: El valor final de la secuencia (no se incluye en la secuencia).
> paso: El incremento entre los números (por defecto es 1).

### Max y Min

```python
mi_lista = [1, 2, 3, 4, 5]
print(max(mi_lista))  # Output: 5
print(min(mi_lista))  # Output: 1
```

```python
cadena = "Python"
print(max(cadena))  # Output: 'y'

cadena = "Python"
print(min(cadena))  # Output: 'P'
```

```python
lista = ["manzana", "banana", "cereza", "uva"]
print(max(lista))  # Output: 'uva'

lista = ["manzana", "banana", "cereza", "uva"]
print(min(lista))  # Output: 'banana'
```

> NOTE
> Las comparaciones de cadenas de texto se hacen carácter por carácter en el orden de sus valores ASCII

### Sorted

```python
mi_lista = [5, 2, 3, 1, 4]
print(sorted(mi_lista))  # Output: [1, 2, 3, 4, 5]
```

### Zip

La función zip() combina varios iterables, emparejando elementos en tuplas.

```python
nombres = ["Juan", "Maria", "Pedro"]
edades = [30, 25, 40]
combinados = zip(nombres, edades)
print(list(combinados))  # Output: [('Juan', 30), ('Maria', 25), ('Pedro', 40)]
```

## Variables

### Arrays

> NOTE
> Los elementos de las listas pueden ser de <u>distintos tipos</u>

#### Declarar una lista vacia

```python
mi_lista = []
```

#### Declarar una lista con valores

```python
lista = [1, 2, 3, 4, 5]
```

#### Añadir un elemento al final de la lista

```python
lista.append(6)
```

#### Eliminar un elemento de la lista por su indice

```python
del lista[2]
```

#### Obtener la longitud de la lista

```python
longitud = len(lista)
```

#### Recorrer una lista

```python
for elemento in lista:
    print(elemento)
```

#### Saber si un elemento se encuentra en la lista

```python
if 3 in lista:
    print("El elemento 3 está en la lista")
```

### Tuplas

> Note
> Son similares a las listas, pero son inmutables, es decir, **no se pueden modificar** después de haber sido creadas.

#### Declarar una tupla

```python
tupla = (1, 2, 3, "cuatro")
```

#### Desempaquetado de una tupla

```python
tupla_empaquetada = 1, 2, 3
a, b, c = tupla_empaquetada
print(a, b, c)
```

### Diccionarios

#### Declarar un diccionario

```python
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

#### Añadir elementos a un diccionario

```python
mi_diccionario["profesion"] = "Programador"
```

#### Eliminar elementos de un diccionario

```python
del mi_diccionario["ciudad"]
```

#### Longitud de un diccionario

```python
longitud = len(mi_diccionario)
```

#### Iterar sobre un diccionario

```python
# Iterar sobre claves
for clave in mi_diccionario:
    print(clave)

# Iterar sobre valores
for valor in mi_diccionario.values():
    print(valor)

# Iterar sobre pares clave-valor
for clave, valor in mi_diccionario.items():
    print(clave, valor)
```

### Conjuntos

#### Declarar un conjunto

```python
mi_conjunto = {1, 2, 3, 4, 5}
```

#### Declarar un conjunto vacio

```python
conjunto_vacio = set()
```

#### Añadir elementos a un conjunto

```python
mi_conjunto.add(6)
```

#### Eliminar elementos de un conjunto

```python
mi_conjunto.remove(3)
```

#### Iteracion sobre un conjunto

```python
for elemento in mi_conjunto:
    print(elemento)
```

#### Unir conjuntos

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)
```

#### Interseccion entre dos conjuntos

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccion = conjunto1.intersection(conjunto2) #Output: 3
```

#### Diferencia entre dos conjuntos

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia  = conjunto1.difference(conjunto2) # Output: {1, 2}
```

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia  = conjunto2.difference(conjunto1) # Output: {4, 5}
```

> NOTE
> Cuando hacemos `conjunto1.difference(conjunto2)`, obtenemos los elementos que están en _conjunto1_ pero no en _conjunto2_. Si hacemos `conjunto2.difference(conjunto1)` obtenemos los elementos que están en _conjunto2_ pero no en _conjunto1_.

## Estructuras de control

### If

```python
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### While

```python
contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1
```

### For

```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

```python
for contador in range(5):
    print("El contador es:", contador)
```

## Funciones

```python
def suma(a, b):
    """Esta función devuelve la suma de dos números."""
    return a + b

print(suma(2, 3))
```

```python
def saludar(nombre):
    """Esta función imprime un saludo."""
    print("¡Hola,", nombre, "!")

saludar("juan")
```

### Desempaquetado de Argumentos

```python
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)  # Output: 15
```

> NOTE
> Puedes pasar un número variable de argumentos a una función utilizando `*args`. Esto permite que una función acepte cualquier número de argumentos posicionales.

### Argumentos de Palabras Clave Arbitrarios

```python
def imprimir_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(clave + ":", valor)

imprimir_informacion(nombre="Juan", edad=30, ciudad="Ciudad de México")
```

> NOTE
> De manera similar al desempaquetado de argumentos, puedes pasar un número variable de argumentos de palabras clave utilizando `**kwargs`.

### Documentación de funciones

```python
def suma(a, b):
    """Esta función devuelve la suma de dos números."""
    return a + b

help(suma) # Muestra la cadena de documentación de la función
```

## Objetos

### Definir una clase

```python
class Persona:
    def __init__(self, nombre, edad): # Contructor
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
```

### Crear un objeto

```python
juan = Persona("Juan", 30)
```

### Acceder a los atributos del objeto:

```python
print(juan.nombre)
```

### Modificar los atributos de un objeto

```python
juan.nombre = "Juan Carlos"
```

### Comprobar si un objeto tiene un atributo especifico

```python
print(hasattr(juan, "apellidos")) # Output: False
```

### Obtener el valor de un atributo si existe o si no devolver un mensaje predefinido

```python
print(getattr(juan, "apellidos", "El objeto 'juan' tiene apellidos definidos"))
# Output: El objeto 'juan' no tiene apellidos definido
```

### Ordenar objetos

```python
personas_ordenadas = sorted(personas, key=lambda x: x.edad)

personas.sort(key=lambda x: x.edad)
```

## Manejo de ficheros y directorios

### Crear un directorio

```python
import os

os.makedirs("nombre_directorio")
```

### Crear un archivo

```python
nombre_archivo = "nuevo_archivo.txt"

with open(nombre_archivo, 'w') as archivo:
    archivo.write("Este es el contenido del archivo.\n")
```

### Listar el contenido de un directorio

```python
contenido_directorio = os.listdir()

for elemento in contenido_directorio:
    print(elemento)
```

### Listar el contenido de un directorio y el contenido de sus subdirectorios

```python
import os

def listar_contenido_directorio(directorio):
    for directorio_actual, subdirectorios, archivos in os.walk(directorio):
        print(f"Contenido de {directorio_actual}:")

        for archivo in archivos:
            print(os.path.join(directorio_actual, archivo))

        for subdirectorio in subdirectorios:
            print(os.path.join(directorio_actual, subdirectorio))

directorio = "ruta/al/directorio"

listar_contenido_directorio(directorio)
```

### Renombrar un archivo o directorio

```python
import os

nombre_original = "antiguo_nombre.txt"
nuevo_nombre = "nuevo_nombre.txt"

os.rename(nombre_original, nuevo_nombre)
```

### Eliminar un archivo

```python
import os

nombre_archivo_a_eliminar = "archivo_a_eliminar.txt"

os.remove(nombre_archivo_a_eliminar)
```

### Eliminar un directorio y su contenido

```python
import shutil

nombre_directorio_a_eliminar = "directorio_a_eliminar"

shutil.rmtree(nombre_directorio_a_eliminar)
```

### Mover archivo

```python
import shutil

ubicacion_original = "ruta/al/archivo/original.txt"
ubicacion_destino = "ruta/a/la/ubicacion/de/destino/archivo.txt"

shutil.move(ubicacion_original, ubicacion_destino)
```

### Mover directorio

```python
ubicacion_directorio_original = "ruta/al/directorio/original"
ubicacion_directorio_destino = "ruta/a/la/ubicacion/de/destino/directorio"

shutil.move(ubicacion_directorio_original, ubicacion_directorio_destino)
```

## Lectura de ficheros

### Leer todo el contenido del fichero como una cadena de texto

```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

### Leer un archivo linea a linea

```python
with open("archivo.txt", "r") as archivo:
    linea = archivo.readline()
    while linea:
        print(linea, end="")
        linea = archivo.readline()
```

### Obtener una lista con las lineas del archivo

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

### Lectura de archivos binarios

```python
with open("archivo.bin", "rb") as archivo_binario:
    datos = archivo_binario.read()
```

### Lectura de ficheros CSV

#### Leer el archivo CSV linea a linea

```python
import csv

with open("datos.csv", newline="") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    for fila in lector_csv:
        print(fila)
```

#### Almacenarlo en un diccionario

```python
import csv

datos_diccionario = []

with open("datos.csv", newline="") as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)

    for fila in lector_csv:
        datos_diccionario.append(fila)
```

#### Almacenarlo en una coleccion de objetos

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

## Escritura de ficheros

### Escribir en un archivo de texto

```python
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.write("Este es un archivo de texto generado por Python.\n")
    archivo.write("Adiós, mundo!")
```

### Agregar contenido a un archivo existente

```python
with open("archivo.txt", "a") as archivo:
    archivo.write("\n¡Esto se añade al final del archivo!")
```

### Escribir en un archivo CSV

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

## Lectura y escritura de objetos usando pickle

### Lectura

```python
import pickle

with open("objetos.pkl", "rb") as archivo:
    personas_recuperadas = pickle.load(archivo)

for persona in personas_recuperadas:
    print(persona.nombre, persona.edad)
```

### Escritura

```python
import pickle

personas = [juan, maria, pedro]

with open("objetos.pkl", "wb") as archivo:
    pickle.dump(personas, archivo)
```

## Bases de datos

### SQLite

```python
import sqlite3
```

#### Conectar a una base de datos

```python
conexion = sqlite3.connect('ejemplo.db')
```

#### Crear un cursor

```python
cursor = conexion.cursor()
```

#### Crear una tabla

```python
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    edad INTEGER
                )''')
```

#### Insertar datos

```python
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 30))
```

#### Guardar los cambios

```python
conexion.commit()
```

#### Obtener datos

```python
cursor.execute("SELECT * FROM usuarios")

filas = cursor.fetchall()
```

###3 Cerrar la conexión

```python
conexion.close()
```

### PostgreSQL

> NOTE
> Hay que instalar previamente _psycopg2_

```sh
pip install psycopg2
```

```python
import psycopg2
```

#### Conectar a una base de datos

```python
conexion = psycopg2.connect(
    host="localhost",
    database="nombre_de_la_base_de_datos",
    user="nombre_de_usuario",
    password="contraseña"
)
```

#### Crear un cursor

```python
cursor = conexion.cursor()
```

#### Crear una tabla

```python
cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre TEXT,
            edad INTEGER
        )
    """)
```

#### Insertar datos

```python
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Juan", 30))
```

#### Guardar los cambios

```python
conexion.commit()
```

#### Obtener datos

```python
cursor.execute("SELECT * FROM usuarios")

filas = cursor.fetchall()
```

#### Cerrar la conexión

```python
conexion.close()
```

#### Excepciones

```python
Exception, psycopg2.Error
```

### MySQL

> NOTE
> Hay que instalar previamente _mysql-connector-python_

```sh
pip install mysql-connector-python
```

```python
import mysql.connector
```

#### Conectar a una base de datos

```python
conexion = mysql.connector.connect(
    host="localhost",
    database="nombre_de_la_base_de_datos",
    user="nombre_de_usuario",
    password="contraseña"
)
```

#### Crear un cursor

```python
cursor = conexion.cursor()
```

#### Crear una tabla

```python
cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre TEXT,
            edad INTEGER
        )
    """)
```

#### Insertar datos

```python
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Juan", 30))
```

#### Guardar los cambios

```python
conexion.commit()
```

#### Obtener datos

```python
cursor.execute("SELECT * FROM usuarios")

filas = cursor.fetchall()
```

#### Cerrar la conexión

```python
conexion.close()
```

#### Excepciones

```python
mysql.connector.Error
```

### MongoDB

> NOTE
> Hay que instalar previamente _pymongo_

```sh
pip install pymongo
```

```python
from pymongo import MongoClient
```

#### Conectarse a un servidor de MongoDB

```python
cliente = MongoClient('mongodb://localhost:27017/')
```

#### Conectarse a una base de datos en MongoDB

db = cliente['nombre_de_la_base_de_datos']

#### Insertar datos

```python
datos = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Pedro", "edad": 40}
]

coleccion.insert_many(datos)
```

#### Leer datos

```python
coleccion = db['nombre_de_la_coleccion']

documentos = coleccion.find()
```
