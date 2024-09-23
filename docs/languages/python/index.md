---
tags:
  - In development
  - Pending review
  - 23/09/2024
---

# Introducción

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
print(type(123))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
print(type("Hola"))  # Output: <class 'str'>
print(type([1, 2, 3]))  # Output: <class 'list'>
```

## Conversión de tipos

```python
print(int("123"))  # Output: 123
print(float("3.14"))  # Output: 3.14
print(str(123))  # Output: '123'
print(list("Hola"))  # Output: ['H', 'o', 'l', 'a']
```

## Range

La función range() se utiliza para generar una secuencia de números. Comúnmente se usa en bucles for.

```python
range(inicio, fin, paso)
```

!!! note

    `inicio`: El valor inicial de la secuencia (por defecto es 0).  
    `fin`: El valor final de la secuencia (no se incluye en la secuencia).  
    `paso`: El incremento entre los números (por defecto es 1).

## Max y Min

```python
mi_lista = [1, 2, 3, 4, 5]
print(max(mi_lista))  # Output: 5
print(min(mi_lista))  # Output: 1
```

```python
cadena = "python"
print(max(cadena))  # Output: 'y'

cadena = "python"
print(min(cadena))  # Output: 'P'
```

```python
lista = ["manzana", "banana", "cereza", "uva"]
print(max(lista))  # Output: 'uva'

lista = ["manzana", "banana", "cereza", "uva"]
print(min(lista))  # Output: 'banana'
```

!!! note

    Las comparaciones de cadenas de texto se hacen carácter por carácter en el orden de sus valores ASCII

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

## Argumentos de entrada

```python
import argparse

parser = argparse.ArgumentParser(description="Este script demuestra el uso de argparse.")

parser.add_argument('nombre', type=str, help='Tu nombre', default="Pepito Grillo")
parser.add_argument('-e, --edad', type=int, help='Tu edad', required=False)
args = parser.parse_args()

print(args.edad, args.nombre)
```
