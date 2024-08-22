# Angular

## Instalación y creación de un nuevo proyecto

### Intalar node.js

Es recomendable el uso de nvm para el control de versiones, por lo que lo instalaremos en lugar del node.js.

Una vez instalado nvm instalamos la última versión o la que necesitemos para el proyecto en el que vamos a trabajar.

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

### Instalar Angular

Para instalar Angular de forma global tenemos que utilizar el comando:

```sh
npm install -g @angular/cli
```

Para instalar Angular en un proyecto tenemos que utilizar el comando desde la terminal ubicándose en el proyecto:

```sh
npm install @angular/cli
```

### Versiones

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

### Creación de un nuevo proyecto

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

## Navegación

### Rutas

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

Para navegar a una ruta usaremos `[routerLink]="['/route']"`

### Ruta por defecto

Para añadir una ruta por defecto:

```typescript
{ path: '', redirectTo: '/', pathMatch: 'full' },
```

#### Rutas hijas

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

Para navegar a la ruta usaremos `[routerLink]="['/father/child']`.

#### Envio de información en la ruta

Si queremos enviar algún dato en la url para obtenerla en el componente al que se navega:

```typescript
{
   path: 'detail/:detailInfo',
   component: DetailComponent
}
```

Se navega desde el html con `[routerLink]="['/detail', detailInfo]"` en un elemento `<a>`

Para acceder a los parámetros de la ruta primero se debe implementar:

```typescript
import { ActivatedRoute } from '@angular/router';
constructor (private route: ActivatedRoute) {}

const routeParams = this.route.snapshot.paramMap;
const detailInfo = routeParams.get('detailInfo');
```

De tal forma que la ruta para acceder al component sería `father/child`, además de que se aplicaría a través del `<router-outlet></router-outlet>`en caso de haberlo.

La mejor forma de organizar las rutas de una web sería tener tres rutas principales:
- Login
- Registro
- Main: esta sería la ruta padre de todas las demás, de manera que así podríamos tener una página base con su respectivo menú y características comunes y las hijas que las compartirían.

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
