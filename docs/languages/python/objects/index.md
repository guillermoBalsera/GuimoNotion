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
print(getattr(juan, "apellidos", "El objeto 'juan' tiene apellidos definidos"))
# Output: El objeto 'juan' no tiene apellidos definido
```

## Ordenar objetos

```python
personas_ordenadas = sorted(personas, key=lambda x: x.edad)

personas.sort(key=lambda x: x.edad)
```
