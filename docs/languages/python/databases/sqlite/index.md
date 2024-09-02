# SQLite

```python
import sqlite3
```

## Conectar a una base de datos

```python
conexion = sqlite3.connect('ejemplo.db')
```

## Crear un cursor

```python
cursor = conexion.cursor()
```

## Crear una tabla

```python
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    edad INTEGER
                )''')
```

## Insertar datos

```python
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 30))
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