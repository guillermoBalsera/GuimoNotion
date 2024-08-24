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

## Creación de componentes

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

Para generar una nueva *pipe* se utiliza el comando

```sh
ng generate pipe directorio/pipes
```

## Rutas

En el `app-routing.module.ts` se establecen las rutas de la siguiente manera:

```typescript
const routes = [
    {
        path: 'route',
        component: Component
    },
    {
        path: 'route',
        component: Component
    }
];
```

### Ruta por defecto

Para añadir una ruta por defecto:

```typescript
{
    path: '', redirectTo: '/', pathMatch: 'full'
}
```

### Rutas hijas

Si se quiere establecer una ruta como hija de otra:

```typescript
const routes: Routes = [
    {
        path: 'father',
        component: FatherComponent,
        children: [
            {
                path: 'child',
                component: ChildComponent
            }
        ]
    }];
```

De tal forma que la ruta para acceder al `component` sería `father/child`, además de que se aplicaría a través del
`<router-outlet></router-outlet>` en caso de haberlo.

### Envio de información en la ruta

Si queremos enviar algún dato en la url para obtenerla en el componente al que se navega:

```typescript
{
    path: 'detail/:detailInfo', component: DetailComponent
}
```

La mejor forma de organizar las rutas de una web sería tener tres rutas principales:

- Login
- Registro
- Main: esta sería la ruta padre de todas las demás, de manera que así podríamos tener una página base con su respectivo
  menú y características comunes y las hijas que las compartirían.

## Navegación

### Navegar desde html

Para navegar a una ruta usaremos: 

```html
[routerLink]="['/route']"
```

Para navegar a una ruta hija usaremos:

```html
[routerLink]="['/father/child']
```

Para enviar información en la ruta usaremos: 

```html
[routerLink]="['/detail', detailInfo]"`
```

Para acceder a los parámetros de la ruta primero se debe implementar:

```typescript
import {ActivatedRoute} from '@angular/router';

constructor(private route: ActivatedRoute) { }

const routeParams = this.route.snapshot.paramMap;
const detailInfo = routeParams.get('detailInfo');
```

### Navegar desde typescript



## Recursos adicionales

- [Página oficial de Angular][angular-page]
- [Documentación oficial de Angular][angular-docs]
- [GitHub de Angular][angular-git]

[node]: ../../../others/node/index.md
[angular-page]: https://angular.dev/
[angular-docs]: https://v17.angular.io/docs
[angular-git]: https://github.com/angular/angular