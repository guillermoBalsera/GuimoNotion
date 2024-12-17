# Docker para desarrollo

## Crear o editar el `Dockerfile`

```dockerfile
# Cambiar la versión de node por la que necesitemos 
FROM node:20.15.0-alpine 

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 4200 49153

CMD npm run start
```

## Crear o editar el `docker-compose.yml`

```docker-compose
version: "3.7"
services:
    chat:
      build: .
      ports:
        - "4200:4200"
        - "49153:49153"
      volumes:
        - "/app/node_modules"
        - ".:/app"
```

## Editar el `package.json`

```json
"scripts": {
  "ng": "ng",
  "start": "ng serve --host 0.0.0.0 --poll 500",
  "build": "ng build",
  "watch": "ng build --watch --configuration development",
  "test": "ng test"
}
```

## Ejecutar el contenedor

```shell
docker-compose up
```

Cuando termine el proceso ya tendríamos la aplicación servida en el puerto 4200

Si queremos apagar el contenedor:

```shell
docker-compose down
```
