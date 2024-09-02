# MySQL

!!! note
    Hay que instalar previamente _mysql-connector-python_

```sh
pip install mysql-connector-python
```

```python
import mysql.connector
```

## Conectar a una base de datos

```python
conexion = mysql.connector.connect(
    host="localhost",
    database="nombre_de_la_base_de_datos",
    user="nombre_de_usuario",
    password="contraseña"
)
```

## Crear un cursor

```python
cursor = conexion.cursor()
```

## Crear una tabla

```python
cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre TEXT,
            edad INTEGER
        )
    """)
```

## Insertar datos

```python
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Juan", 30))
```

## Guardar los cambios

```python
conexion.commit()
```

## Obtener datos

```python
cursor.execute("SELECT * FROM usuarios")

filas = cursor.fetchall()
```

## Cerrar la conexión

```python
conexion.close()
```

## Excepciones

```python
mysql.connector.Error
```
