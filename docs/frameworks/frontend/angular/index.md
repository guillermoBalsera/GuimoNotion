# Angular

## Instalación y creación de un nuevo proyecto

### Intalar node.js

Lo primero que debemos hacer es instalar [node.js][node] para el manejo de dependencias y la creación del proyecto y sus
respectivos componentes.

### Instalar Angular

Para instalar Angular de forma global tenemos que utilizar el comando:

```sh
npm install -g @angular/cli
```

Para instalar Angular en un proyecto tenemos que utilizar el comando desde la terminal ubicándose en el proyecto:

```sh
npm install @angular/cli
```

Verificamos la instalción son el comando:

```sh
ng version
```

Si no nos permite comprobar la versión de Angular utilizaremos el siguiente comando:

```sh
Set-ExecutionPolicy - ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Creación de un nuevo proyecto

Antes de crear nuestro proyecto debemos decidir que clase de proyecto queremos usar _standalone_ o -clásico_:

- Un proyecto standalone en Angular es una forma más reciente de configurar y desarrollar aplicaciones que permite
  omitir el uso de NgModules para la organización del código. Este enfoque fue introducido en Angular v14 y tiene como
  objetivo simplificar la estructura del proyecto y hacer que el desarrollo de componentes sea más directo y menos
  dependiente de los módulos tradicionales.
- Un proyecto no standalone o clásico es la forma tradicional de construir aplicaciones Angular, utilizando NgModules
  para agrupar componentes, directivas, pipes, y servicios en unidades reutilizables.

Para crear un nuevo proyecto standalone en Angular utilizamos en comando:

```sh
ng new nombreAplicacion
```

Si queremos crear un nuevo proyecto clásico:

```sh
ng new nombreAplicacion --standalone=false
```

El archivo **package.json** muestra las dependencias instaladas, la versión de angular y los comandos habilitados por
Angular en el proyecto.

Para iniciar el proyecto usamos el comando:

```sh 
ng serve
```

## Recursos adicionales

- [Página oficial de Angular][angular-page]
- [Documentación oficial de Angular][angular-docs]
- [GitHub de Angular][angular-git]

[node]: ../../../others/node/index.md
[angular-page]: https://angular.dev/
[angular-docs]: https://v17.angular.io/docs
[angular-git]: https://github.com/angular/angular