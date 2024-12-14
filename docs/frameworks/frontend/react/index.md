---
tags:
- In development
- Pending review
- 24/11/2024
---

# React

React es una biblioteca de javascript que está pensada para construir interfaces de usuario.

Cuando usamos React no estamos escribiendo HTML, sino que estamos escribiendo JSX y el propio react lo compila a javascript.

## Crear una aplicación

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

Entramos en la carpeta que se ha creado con el nombre de nuestro proyecto:

```shell
npm install
```

```shell
npm run dev
```

## Componentes

Los nombres de los componentes deben estar siempre en [PascalCase][pascal]

```jsx
function Calculate() {
    let number = 0;
    
    return (
        <p>Number: {number}</p>
    )
}
```

```jsx
function Input() {
    let myPlaceHolder = "Escribe aquí";
    
    return (
        <input myPlaceholder={placeHolder}/>
    )
}
```

### Estados

Es un estado interno que corresponde a cada componente individualmente.

```jsx
import { useState } from 'react';
```

```jsx
// Le pasamos al useState el valor por defecto de la variable `isFollowing`
const [isFollowing, setIsFollowing] = useState(false);
const handleClick = () => {
    setIsFollowing(!isFollowing)
}
```

```jsx
<button onClick={handleClick}>Button</button>
```

```jsx
function Calculate() {
    const [number, setNumber] = useState(0);
    
    const addOne = () => {
        setNumber(number + 1);
    }
    
    return (
        <div>
            <p>Number: {number}</p>
            <button onClick={addOne}></button>
        </div>
    )
}
```

### Renderizado de listas

```jsx
function MovieList()  {
    const movies = ["Lord of the rings", "Dune", "Shrek"];
    
    const HTMLMovies = movies.map((movie, index) => {
        return (<p key={movie}>{index + 1} - {movie}</p>)
    })
    
    return (
        <section>
            {HTMLMovies}
        </section>
    )
}
```

Para renderizar una lista de objetos:

```jsx
function MovieList()  {
    const animal = [{id: 1, name: "dog", species: "mamal"}, {id: 2, name: "shark", species: "fish"}];
    
    const HTMLAnimals = animal.map((animal) => {
        return (<li key={animal.id}>{animal.name}</li>)
    })
    
    return (
        <section>
            {HTMLAnimals}
        </section>
    )
}
```

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

### Ciclos de vida de los componentes

- **Mount**: Cada vez que aparece en la página.
- **Updates**: Cada vez que el estado cambia.
- **Unmount**: Cuando se elimina de la página.

!!! note ""

    El DOM virtual hace que cuando se produce un cambio lo único que modifica en el DOM es la parte que ha recibido un cambio.

    Cada vez que se realiza un cambio en un estado React identifica que debe renderizar de nuevo las partes que han cambiado.

    La otra forma de volver a renderizar de nuevo un componente es que su componente padre se vuelva a renderizar.


[node]: ../../../others/node/index.md
[vite]: https://vite.dev/
[pascal]:   ../../../others/cases/index.md





Pastillas:
 - 6 