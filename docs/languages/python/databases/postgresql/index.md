# PostgreSQL

!!! note

    Hay que instalar previamente _psycopg2_

```sh
pip install psycopg2
```

```python
import psycopg2
```

## Conectar a una base de datos

```python
conexion = psycopg2.connect(
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
Exception, psycopg2.Error
```
