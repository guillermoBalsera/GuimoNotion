

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

constructor(private route: ActivatedRoute) { }

const routeParams = this.route.snapshot.paramMap;
const detailInfo = routeParams.get('detailInfo');
```

### Navegar desde typescript