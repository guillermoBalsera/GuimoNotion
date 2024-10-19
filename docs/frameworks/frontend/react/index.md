---
tags:
- In development
- Pending review
- 19/10/2024
---

# React

React es una biblioteca de javascript que está pensada para construir interfaces de usuario.

Cunado usamos React no estamos escribiendo HTML sino que estamos escribiendo JSX y el propio react lo compila a javascript.

## Crear una aplicación

### Intalar node.js

Lo primero que debemos hacer es instalar [node.js][node] para el manejo de dependencias y la creación del proyecto y sus
respectivos componentes.

Para crear nuestro proyecto vamos a usar [Vite][vite]

```shell
npm init -y
```

```shell
npm create vite@latest
```

Escogeremos la opción `JavaScript + SWC`

```shell
npm run dev
```

## Componentes

Los nombres de los componentes deben estar siempre en [PascalCase][pascal]


[vite]: https://vite.dev/
[pascal]: ../../../others/cases/index.md

