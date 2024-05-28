<div align="center">
   <img src="../0-Assets/logo.png" alt="Descripción de la imagen" width="200px" height="200px">
   <h1>PYTHON</h1>
</div>

---

# Funcionalidades básicas

## Print
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

## Input
```python
nombre = input("¿Cuál es tu nombre? ")
```

## Longitud
```python
mi_lista = [1, 2, 3, 4, 5]
print(len(mi_lista))  # Output: 5
```

## Type
```python
print(type(123))          # Output: <class 'int'>
print(type(3.14))         # Output: <class 'float'>
print(type("Hola"))       # Output: <class 'str'>
print(type([1, 2, 3]))    # Output: <class 'list'>
```

## Conversión de tipos
```python
print(int("123"))       # Output: 123
print(float("3.14"))    # Output: 3.14
print(str(123))         # Output: '123'
print(list("Hola"))     # Output: ['H', 'o', 'l', 'a']
```

## Range
La función range() se utiliza para generar una secuencia de números. Comúnmente se usa en bucles for.
```python
range(inicio, fin, paso)
```
> NOTE
> inicio: El valor inicial de la secuencia (por defecto es 0).
> fin: El valor final de la secuencia (no se incluye en la secuencia).
> paso: El incremento entre los números (por defecto es 1).
 
## Max y Min
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

## Sorted
```python
mi_lista = [5, 2, 3, 1, 4]
print(sorted(mi_lista))  # Output: [1, 2, 3, 4, 5]
```

## Zip
La función zip() combina varios iterables, emparejando elementos en tuplas.
```python
nombres = ["Juan", "Maria", "Pedro"]
edades = [30, 25, 40]
combinados = zip(nombres, edades)
print(list(combinados))  # Output: [('Juan', 30), ('Maria', 25), ('Pedro', 40)]
```

# Variables

## Arrays
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

## Tuplas
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

## Diccionarios

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

## Conjuntos

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
> Cuando hacemos `conjunto1.difference(conjunto2)`, obtenemos los elementos que están en *conjunto1* pero no en *conjunto2*. Si hacemos `conjunto2.difference(conjunto1)` obtenemos los elementos que están en *conjunto2* pero no en *conjunto1*.

# Estructuras de control

## If

```python
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## While

```python
contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1
```

## For

```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

```python
for contador in range(5):
    print("El contador es:", contador)
```

# Objetos

## Definir una clase
```python
class Persona:
    def __init__(self, nombre, edad): # Contructor
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
```

## Crear un objeto
```python
juan = Persona("Juan", 30)
```

## Acceder a los atributos del objeto:
```python
print(juan.nombre)
```

## Modificar los atributos de un objeto
```python
juan.nombre = "Juan Carlos"
```

## Comprobar si un objeto tiene un atributo especifico
```python
print(hasattr(juan, "apellidos")) # Output: False
```

## Obtener el valor de un atributo si existe o si no devolver un mensaje predefinido
```python
print(getattr(juan, "apellidos", "El objeto 'juan' tiene apellidos definidos")) # Output: El objeto 'juan' no tiene apellidos definido
```

## Ordenar objetos
```python
personas_ordenadas = sorted(personas, key=lambda x: x.edad)

personas.sort(key=lambda x: x.edad)
```


