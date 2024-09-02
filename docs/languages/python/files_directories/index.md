# Manejo de ficheros y directorios

## Crear un directorio

```python
import os

os.makedirs("nombre_directorio")
```

## Crear un archivo

```python
nombre_archivo = "nuevo_archivo.txt"

with open(nombre_archivo, 'w') as archivo:
    archivo.write("Este es el contenido del archivo.\n")
```

## Listar el contenido de un directorio

```python
contenido_directorio = os.listdir()

for elemento in contenido_directorio:
    print(elemento)
```

## Listar el contenido de un directorio y el contenido de sus subdirectorios

```python
import os

def listar_contenido_directorio(directorio):
    for directorio_actual, subdirectorios, archivos in os.walk(directorio):
        print(f"Contenido de {directorio_actual}:")

        for archivo in archivos:
            print(os.path.join(directorio_actual, archivo))

        for subdirectorio in subdirectorios:
            print(os.path.join(directorio_actual, subdirectorio))

directorio = "ruta/al/directorio"

listar_contenido_directorio(directorio)
```

## Renombrar un archivo o directorio

```python
import os

nombre_original = "antiguo_nombre.txt"
nuevo_nombre = "nuevo_nombre.txt"

os.rename(nombre_original, nuevo_nombre)
```

## Eliminar un archivo

```python
import os

nombre_archivo_a_eliminar = "archivo_a_eliminar.txt"

os.remove(nombre_archivo_a_eliminar)
```

## Eliminar un directorio y su contenido

```python
import shutil

nombre_directorio_a_eliminar = "directorio_a_eliminar"

shutil.rmtree(nombre_directorio_a_eliminar)
```

## Mover archivo

```python
import shutil

ubicacion_original = "ruta/al/archivo/original.txt"
ubicacion_destino = "ruta/a/la/ubicacion/de/destino/archivo.txt"

shutil.move(ubicacion_original, ubicacion_destino)
```

## Mover directorio

```python
ubicacion_directorio_original = "ruta/al/directorio/original"
ubicacion_directorio_destino = "ruta/a/la/ubicacion/de/destino/directorio"

shutil.move(ubicacion_directorio_original, ubicacion_directorio_destino)
```
