# Funciones

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

## Desempaquetado de Argumentos

```python
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)  # Output: 15
```

!!! note
    Puedes pasar un número variable de argumentos a una función utilizando `*args`. Esto permite que una función acepte cualquier número de argumentos posicionales.

## Argumentos de Palabras Clave Arbitrarios

```python
def imprimir_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(clave + ":", valor)

imprimir_informacion(nombre="Juan", edad=30, ciudad="Ciudad de México")
```

!!! note
    De manera similar al desempaquetado de argumentos, puedes pasar un número variable de argumentos de palabras clave utilizando `**kwargs`.

## Documentación de funciones

```python
def suma(a, b):
    """Esta función devuelve la suma de dos números.
    :param int a: El primer número que se suma
    :param int b: El segundo número que se suma
    :return: La suma de ambos números 
    """
    return a + b

help(suma) # Muestra la cadena de documentación de la función
```
