## Componentes

Para generar un nuevo `component` usamos el comando:

```sh
ng generate component directorio/nombreComponente
```

### Estructura de un componente

```typescript
@Component({
    standalone: true, /* standalone representa si se trata de un componente standalone o clásico en caso de no aparecer */
    selector: 'app-component', /* selector representa la forma de llamar al componente desde el html de otro */
    templateUrl: './component.component.html', /* templateUrl representa la url donde se ubica la template del componente */
    styleUrl: './component.component.css', /* styleUrl representa la url donde se ubica el archivo que define los estilos del componente */
})
export class Component {
    /* Aquí se define el comportamiento del componente */
}
```

La template de un componente puede sustituirse directamente por html sin necesidad de un archivo html:

```typescript
@Component({
    selector: 'app-component',
    templateUrl: '<h1>Hello World!</h1>',
    styleUrl: './component.component.css',
})
export class Component {
}
```

!!! note ""
    
    Es recomendable cambiar el nombre del selector a los componentes:
    ```typescript 
    selector: 'Component'
    ```


### LLamar a un componente desde otro

Si el proyecto es standalone debemos importar el componente que vamos a usar dentro del componente desde el que lo
llamaremos:

```typescript
import {Component} from './todo-list-item.component.ts';

@Component({
    standalone: true,
    imports: [Component],
    template: `
    <ul>
      <app-component></app-component>
    </ul>
  `,
})
export class MainComponent {
}
```

Si el proyecto es clásico debemos importar el componente en `app-module.ts`

```typescript
import {Component} from './todo-list-item.component.ts';

@NgModule({
    declarations: [
        AppComponent,
        Component
        /* Debe declararse para poder ser usado en el proyecto y sus componentes */
    ],
    imports: [
        BrowserModule,
        AppRoutingModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
```
