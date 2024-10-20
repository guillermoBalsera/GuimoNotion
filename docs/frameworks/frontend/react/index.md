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

### Proyección de contenido

Cuando queremos proyectar contenido dentro de un componente debemos usar la palabra reservada `children`.

```jsx
export function Card({children}) {
    return (
        <div className="card">
            { children }
        </div>
    )
}
```

```jsx
export function App() {
    return (
        <Card>
            <p>Este contenido se proyectará dentro del componente Card</p>
        </Card>
    )
}
```

Para pasar todos los props como un solo objeto se hace de la siguiente manera:

```jsx
const object = { a: true, b: 'b'}
return (
    <Component {...object}></Component>
)
```

Aunque esto último no es una buena práctica.

### Estados

Es un estado interno que corresponde a cada componente individualmente.

```jsx
import { useState } from 'react';
```

```jsx
const [isFollowing, setIsFollowing] = useState(false);
const handleClick = () => {
    setIsFollowing(!isFollowing)
}
```

```jsx
<button onClick={handleClick}>Button</button>
```

!!! note ""

    El DOM virtual hace que cuando se produce un cambio lo único que modifica en el DOM es la parte que ha recibido un cambio.

    Cada vez que se realiza un cambio en un estado React identifica que debe renderizar de nuevo las partes que han cambiado.

    La otra forma de volver a renderizar de nuevo un componente es que su componente padre se vuelva a renderizar.



[vite]: https://vite.dev/
[pascal]:   ../../../others/cases/index.md

