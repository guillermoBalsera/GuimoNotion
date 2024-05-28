<div align="center">
   <img src="../0-Assets/logo.png" alt="Descripción de la imagen" width="200px" height="200px">
   <h1>ANGULAR</h1>
</div>

---

# 1. Instalación y creación de un nuevo proyecto

## Intalar node.js

Es recomendable el uso de nvm para el control de versiones, por lo que lo instalaremos en lugar del node.js.

Una vez instalado nvm instalamos la ultima versión o la que necesitemos para el proyecto en el que vamos a trabajar.

Podemos obtener una lista de las versiones disponibles usando el comando: 

```sh
nvm ls available
```

Para instalar la versión de node utilizaremos el siguiente comando sustituyendo el número por la versión que nosotros deseemos: 

```sh
nvm install 20.0.0
```

Para obtener una lista de las versiones disponibles instaladas previamente podemos utilizar el comando:

```sh
nvm ls
```

Para indicar que versión queremos utilizar usaremos el siguiente comando sustituyendo el número por la versión que nosotros deseemos usar de la lista de versiones disponibles ya instaladas previamente:

```sh
nvm use 20.0.0
```

## Instalar Angular

Para instalar Angular de forma global tenemos que utilizar el comando:

```sh
npm install -g @angular/cli
```

Para instalar Angular en un proyecto tenemos que utilizar el comando:

```sh
npm install @angular/cli
```

## Versiones

Comandos para el control de versiones:

- nvm
```sh
nvm version
```

- node.js
```sh
node -v
```

- npm
```sh
npm -v
```

- Angular
```sh
ng version
```

Si no nos permite comprobar la versión de Angular utilizaremos el siguiente comando:

```sh
Set-ExecutionPolicy - ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Creación de un nuevo proyecto

Para crear un nuevo proyecto standalone en Angular utilizamos en comando:

```sh
ng new nombreAplicacion
```

Si queremos crear un nuevo proyecto sin que sea standalone usamos:

```sh
ng new nombreAplicacion --standalone=false
```

El archivo **package.json** muestra las dependencias instaladas, la versión de angular y los comandos habilitados por Angular en el proyecto.

Para iniciar el proyecto usamos el comando:

```sh 
ng serve
```

# Rutas

En el `app-routing.module.ts` se establecen las rutas de la siguiente manera:

```typescript
const routes = [
   {
      path: 'nombre-ruta',
      component: NombreComponente
   },
   {
      path: 'nombre-ruta',
      component: NombreComponente
   }
];
```

Para generar un nuevo *component* usamos el comando:

```sh
ng generate component directorio/nombreComponente
```

Para generar un nuevo *module* se usa el comando:

```sh
ng generate module directorio/nombreModulo
```

Para generar un nuevo *service* se utiliza el comando:

```sh
ng generate service directorio/nombreServicio
```

