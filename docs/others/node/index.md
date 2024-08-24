# Node.js

## ¿Qué es Node.js?

Node.js es un entorno de ejecución para JavaScript que se construyó sobre el motor JavaScript V8 de Chrome. Permite a
los desarrolladores ejecutar código JavaScript en el servidor, fuera del navegador, para construir aplicaciones backend
escalables.

### Características principales de Node.js:

- Asíncrono y orientado a eventos: Node.js utiliza un modelo de entrada/salida no bloqueante, lo que lo hace eficiente y
  adecuado para aplicaciones en tiempo real.
- Motor V8: Utiliza el motor V8 de Google Chrome para ejecutar código JavaScript rápidamente.
- Ecosistema de npm: Node.js viene con npm, un gestor de paquetes que ofrece una gran cantidad de módulos para agilizar
  el desarrollo.

## Instalación de node.js

Es recomendable el uso de [nvm][nvm] para el control de versiones, por lo que lo instalaremos en lugar del node.js. Si
tenemos node.js instalado, lo mejor es desinstalarlo.

Verifica la instalación de nvm con el comando:

```shell
nvm version
```

Una vez instalado nvm instalamos la última versión o la que necesitemos para el proyecto en el que vamos a trabajar.

Podemos obtener una lista de las versiones disponibles usando el comando:

```sh
nvm ls available
```

Para instalar la versión de node utilizaremos el siguiente comando sustituyendo el número por la versión que nosotros
deseemos:

```sh
nvm install 20.0.0
```

Para obtener una lista de las versiones disponibles instaladas previamente podemos utilizar el comando:

```sh
nvm ls
```

Para indicar que versión queremos utilizar usaremos el siguiente comando sustituyendo el número por la versión que
nosotros deseemos usar de la lista de versiones disponibles ya instaladas previamente:

```sh
nvm use 20.0.0
```

Verifica que funciona con el comando:

```sh
npm -v
```

## Ejecutar un script

```shell
node app.js
```

## Inicializar un proyecto

```shell
npm init
```

## Instalar un paquete

```shell
npm install <nombre_paquete>
```

## Instalar un paquete de manera global

```shell
npm install -g <nombre_paquete>
```

## Desinstalar un paquete

```shell
npm uninstall <nombre_paquete>
```

## Recursos Adicionales

- [Documentación de npm][npm]
- [Documentación Oficial de Node.js][node]


[nvm]: https://github.com/nvm-sh/nvm
[npm]: https://docs.npmjs.com/
[node]: https://nodejs.org