## Componentes

Para generar un nuevo *component* usamos el comando:

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

### Manipulación del html

Para mostrar datos en el html usaremos:

```typescript
title = 'this is the title';
```

```html
<h1> {{ title }} </h1>
```

Si queremos usar una variable dentro de una etiqueta html para alterar el estilo:

```typescript
color = 'red';
```

```html
<p [style.color]="color"></p>
```

Si queremos mostrar un dato en el html y que a su vez si en el html se modifica se actualice nuestra variable en el typescript
, se utiliza `two-way-databiding`:

```typescript
name = 'William Shakespeare'
```

```html
<input type="text" [(ngModel)]="name">
```

> Para usar `ngModel` debemos importar `FormsModule` y añadirlo a las importaciones del `app-module.ts`

#### Bucles y condicionales dentro del html

Existen dos formas de hacer bucles y condicionales en el html:

##### ngIf y ngFor

```typescript
nameList = [{name: 'name1', surname: 'surname1'}, {name: 'name2', surname: 'surname2'}];
```

```html
<ng-container *ngIf="nameList.length > 0 ">
    <ng-container *ngFor="let item of list; index as i">
        <p> {{ i }} - {{ item.name }}</p>
    </ng-container>
</ng-container>
```

- ngIf solo muestra el contenido si la longitud de la lista es mayor que 0
- ngFor: por cada elemento de la lista muestra una etiqueta <p> con el `name` del objeto sobre el que está iterando. 
- La variable `index` del ngFor representa el número de iteraciones, aunque no es obligatorio usarla es recomendable en muchas ocasiones.

##### @if y @for























