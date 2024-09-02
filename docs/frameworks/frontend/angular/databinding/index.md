
# Databinding

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

!!! warning
    Para usar `ngModel` debemos importar `FormsModule` y añadirlo a las importaciones del `app-module.ts`

## Bucles y condicionales dentro del html

Existen dos formas de hacer bucles y condicionales en el html que explicaremos mediante ejemplos:

### ngIf y ngFor

```typescript
nameList = [{name: 'name1', surname: 'surname1'}, {name: 'name2', surname: 'surname2'}];
```

```html
<ng-container *ngIf="nameList.length > 0">
    <ng-container *ngFor="let item of nameList; index as i">
        <p> {{ i }} - {{ item.name }}</p>
    </ng-container>
</ng-container>
```

- ngIf solo muestra el contenido si la longitud de la lista es mayor que 0
- ngFor: por cada elemento de la lista muestra una etiqueta <p> con el `name` del objeto sobre el que está iterando. 
- La variable `index` del ngFor representa el número de iteraciones, aunque no es obligatorio usarla es recomendable en muchas ocasiones.

### @if y @for

```html
@if (nameList.length < 100) {      
    @for (item of nameList; track item; 
            let i = $index, first = $first, last = $last, 
            odd = $odd, even = $even, count = $count) {
        <p> {{ i }} - {{ item.name }} - {{ first }} - {{ last }} - {{ odd }} - {{ even }} - {{ count }} </p>
    }  
    @empty {
        <li>No hay items en la lista</li>
    }
} @else {      
    <p>Aquí hay demasiada gente</p>    
}
```

- `@if`: solo muestra los datos si la lista tiene menos de 100 elementos
- `@for`: muestra un parrafo por cada elemento de la lista sobre la que se itera
- `$index`: representa el número de iteración en el que se encuentra el elemento
- `$first`: represente si es el primer elemento de la lista
- `$last`: representa si es el último elemento de la lista
- `$odd`: representa si la iteracion es impar con respecto al `$index`
- `$even`: representa si la iteracion es par con respecto al `$index`
- `$count`: representa el número de iteraciones totales
- `@empty`: muestra los datos si la coleccioón sobre la que se está iterando está vacía
- `@else`: muestra los datos si no se cumple la condición del `@if`






















