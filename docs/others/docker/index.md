---
tags:
  - In development
  - Pending review
  - 11/11/2024
---

# Docker

Docker es una plataforma de virtualización a nivel de sistema operativo que permite crear, implementar y ejecutar
aplicaciones en contenedores ligeros y portátiles. Un contenedor es una instancia de una imagen que incluye el software
necesario para que una aplicación se ejecute de manera consistente en cualquier entorno.

## Comandos básicos de Docker

| Comando                | Descripción                                        |
|:-----------------------|:---------------------------------------------------|
| `docker --version`     | Muestra la versión de Docker instalada             |
| `docker info`          | Muestra información sobre la instalación de Docker |
| `docker pull <imagen>` | Descarga una imagen de Docker Hub                  |
| `docker images`        | Lista todas las imágenes locales                   |
| `docker ps`            | Lista los contenedores en ejecución                |
| `docker ps -a`         | Lista todos los contenedores (activos e inactivos) |
| `docker start <id>`    | Inicia un contenedor parado                        |
| `docker stop <id>`     | Detiene un contenedor en ejecución                 |
| `docker rm <id>`       | Elimina un contenedor                              |
| `docker rmi <imagen>`  | Elimina una imagen                                 |

## Trabajar con Imágenes

Las imágenes son plantillas que definen el contenido de un contenedor. Docker Hub es el registro oficial donde puedes
encontrar y descargar imágenes.

### Buscar y descargar una imagen

Para buscar una imagen en Docker Hub:

```shell
docker search <nombre_imagen>
```

Para descargar una imagen:

```shell
docker pull <nombre_imagen>
```

Para listar todas las imágenes descargadas:

```shell
docker images
```

## Contenedores en docker

Los contenedores son instancias de imágenes en ejecución que crean un entorno aislado.

### Crear y ejecutar un contenedor

Para ejecutar un contenedor de forma interactiva:

```shell
docker run -it <nombre_imagen> /bin/bash
```

Para ejecutar un contenedor en segundo plano:

```shell
docker -run -d --name <nombre_contenedor> <nombre_imagen>
```

### Inspeccionar un Contenedor

Para ver detalles de un contenedor:

```shell
docker inspect <id_contenedor>
```

### Eliminar contenedores

Para detener un contenedor en ejecución:

```shell
docker stop <id_contenedor>
```

Para eliminar un contenedor detenido:

```shell
docker rm <id_contenedor>
```

## Dockerfile y Construcción de Imágenes Personalizadas

Un Dockerfile es un archivo de texto que contiene las instrucciones para crear una imagen personalizada.

### Crear un Dockerfile

Ejemplo de Dockerfile para una aplicación de Node.js:

```dockerfile
# Especificar la imagen base
FROM node:14

# Crear y establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY . .

# Instalar dependencias
RUN npm install

# Exponer el puerto
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["node", "app.js"]
```

### Construir una Imagen desde un Dockerfile

Para construir una imagen desde un `Dockerfile`:

```shell
docker build -t <nombre_imagen> .
```

### Ejecutar una imagen creada

```shell
docker run -d -p 3000:3000 mi_app_node
```

## Docker Compose

Docker Compose permite definir y ejecutar aplicaciones multicontenedor en Docker usando un archivo `docker-compose.yml`.

### Ejemplo de Archivo docker-compose.yml

Ejemplo de un `docker-compose.yml` para una aplicación web con una base de datos MySQL:

```yaml
version: '3'
services:
  web:
    image: my_web_app
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "80:80"
    depends_on:
      - db

  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: my_database
```

### Comandos básicos de Docker Compose

| Comando               | Descripción                                   |
|:----------------------|:----------------------------------------------|
| `docker-compose up`   | Crea y levanta los contenedores especificados |
| `docker-compose down` | Detiene y elimina los contenedores            |
| `docker-compose ps`   | {Lista los contenedores manejados por Compose |

Para levantar todos los servicios definidos en `docker-compose.yml`:

```shell
docker-compose up -d
```

Para detener todos los servicios:

```shell
docker-compose down
```

