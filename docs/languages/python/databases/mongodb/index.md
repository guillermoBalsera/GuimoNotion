# MongoDB

!!! note
    Hay que instalar previamente _pymongo_

```sh
pip install pymongo
```

```python
from pymongo import MongoClient
```

## Conectarse a un servidor de MongoDB

```python
cliente = MongoClient('mongodb://localhost:27017/')
```

## Conectarse a una base de datos en MongoDB

db = cliente['nombre_de_la_base_de_datos']

## Insertar datos

```python
datos = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Pedro", "edad": 40}
]

coleccion.insert_many(datos)
```

## Leer datos

```python
coleccion = db['nombre_de_la_coleccion']

documentos = coleccion.find()
```
