

# Rutas

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

## Ruta por defecto

Para añadir una ruta por defecto:

```typescript
{
    path: '', redirectTo: '/', pathMatch: 'full'
}
```

## Rutas hijas

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

## Envio de información en la ruta

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
```

```typescript
constructor(private route: ActivatedRoute) { }
```

```typescript
const routeParams = this.route.snapshot.paramMap;
const detailInfo = routeParams.get('detailInfo');
```

### Navegar desde typescript

La ruta debe ser en formato String y debe estar estructurada como se ha visto previamente en la navegación desde html.

```typescript
import {Router} from "@angular/router";
```

```typescript
  constructor(private router: Router) { }
```

```typescript
this.router.navigate([route])
      .then(() => console.log(`Correct navigation: ${route}`))
      .catch(err => console.log(`ERROR\t${err}`));
```

!!! tip ""

    Es recomendable el uso de un servicio para utilizar la navegación desde typescript para evitar repetir codigo, 
    dado que con el mismo método en un servicio podemos navegar desde todos lo componentes tan solo inyectando el 
    servicio en el constructor del propio componente.

Para enviar información en la ruta:

```typescript
this.router.navigate(['user', id])
.then(() => console.log(`Correct navigation to user with id: ${id}`))
.catch(err => console.log(`ERROR\t${err}`));
```

Obtendremos esta información del mismo modo que hemos visto anteriormente al enviar información por html.

Otra forma de enviar información en la ruta sería con `query params`:

```typescript
this.router.navigate(['user'], { queryParams: { id: id, name: name } })
  .then(() => console.log(`Correct navigation with query params: ${id}, ${name}`))
  .catch(err => console.log(`ERROR\t${err}`));
```

Y obtendremos las variables:

```typescript
import {ActivatedRoute} from '@angular/router';
```

```typescript
constructor(private route: ActivatedRoute) { }
```

```typescript
this.route.queryParams.subscribe(params => {
  this.id = params['id'];
});
```