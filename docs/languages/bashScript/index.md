---
tags:
  - Pending review
  - 02/09/2024
---

## Introducción

Bash es un intérprete de comandos de Unix que también se puede usar para escribir scripts. Los scripts de Bash permiten
automatizar tareas en sistemas Unix y Linux.

## Estructura de un Script Bash

Un script Bash es un archivo de texto que contiene una serie de comandos que se ejecutan en secuencia. Aquí está la
estructura básica:

```bash
#!/bin/bash

# Comentario: Esto es un comentario en Bash
echo "¡Hola, Mundo!"
```

`#!/bin/bash`: Esta línea, conocida como shebang, indica al sistema que use Bash para interpretar el script.

`echo "¡Hola, Mundo!"`: Imprime el texto en la consola.

## Variables

```bash
#!/bin/bash

nombre="Juan"
echo "Hola, $nombre"
```

## Estructuras de Control

### Condicionales

```bash
#!/bin/bash

edad=18

if [ $edad -ge 18 ]; then
    echo "Eres mayor de edad."
else
    echo "Eres menor de edad."
fi
```

### For

```bash
#!/bin/bash

for i in {1..5}; do
    echo "Número $i"
done
```

### While

```bash
#!/bin/bash

contador=1

while [ $contador -le 5 ]; do
    echo "Contador $contador"
    ((contador++))
done
```

## Funciones

```bash
#!/bin/bash

saludar() {
    echo "Hola, $1"
}

saludar "Mundo"
```

## Manejo de Argumentos

```bash
#!/bin/bash

echo "Primer argumento: $1"
echo "Segundo argumento: $2"
```

## Manejo de Errores

```bash
#!/bin/bash

comando_que_puede_fallar
if [ $? -ne 0 ]; then
    echo "El comando falló."
fi
```

## Lectura de Entrada

```bash
#!/bin/bash

echo "Introduce tu nombre:"
read nombre
echo "Hola, $nombre"
```

## Redirección y pipes

### Redirección de salida

```bash
echo "Texto" > archivo.txt
```

### Redirección de Error: 2> para redirigir errores a un archivo.

```bash
comando_inexistente 2> error.log
```

### Pipes: | para canalizar la salida de un comando a otro.

```bash
ls | grep "archivo"
```

## Recursos adicionales

- [Documentación oficial de bash](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)
- [Tutorial de Bash Scripting](https://linuxconfig.org/bash-scripting-tutorial)

