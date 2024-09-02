# Diccionarios

## Declarar un diccionario

```python
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

## Añadir elementos a un diccionario

```python
mi_diccionario["profesion"] = "Programador"
```

## Eliminar elementos de un diccionario

```python
del mi_diccionario["ciudad"]
```

## Longitud de un diccionario

```python
longitud = len(mi_diccionario)
```

## Iterar sobre un diccionario

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