# Conjuntos

## Declarar un conjunto

```python
mi_conjunto = {1, 2, 3, 4, 5}
```

## Declarar un conjunto vacio

```python
conjunto_vacio = set()
```

## Añadir elementos a un conjunto

```python
mi_conjunto.add(6)
```

## Eliminar elementos de un conjunto

```python
mi_conjunto.remove(3)
```

## Iteracion sobre un conjunto

```python
for elemento in mi_conjunto:
    print(elemento)
```

## Unir conjuntos

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)
```

## Interseccion entre dos conjuntos

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccion = conjunto1.intersection(conjunto2)  # Output: 3
```

## Diferencia entre dos conjuntos

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia = conjunto1.difference(conjunto2)  # Output: {1, 2}
```

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia = conjunto2.difference(conjunto1)  # Output: {4, 5}
```

!!! note

    Cuando hacemos `conjunto1.difference(conjunto2)`, obtenemos los elementos que están en _conjunto1_ pero no en
    _conjunto2_. Si hacemos `conjunto2.difference(conjunto1)` obtenemos los elementos que están en _conjunto2_ pero no en
    _conjunto1_.
