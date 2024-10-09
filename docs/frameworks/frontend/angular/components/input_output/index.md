# Input y Output

## Input

Para enviar un valor desde el componente padre al componente hijo se usa `@Input`:

```typescript
@Component({...})
export class CustomSlider {
    @Input() value = 0;
}
```

```html

<custom-slider [value]="50"/>
```

### Personalizar inputs

#### Inputs requeridos

```typescript
@Component({...})
export class CustomSlider {
    @Input({required: true}) value = 0;
}
```

#### Tranformar inputs

```typescript
@Component({
    selector: 'custom-slider',
    ...
})
export class CustomSlider {
    @Input({transform: trimString}) label = '';
}

function trimString(value: string | undefined) {
    return value?.trim() ?? '';
}
```

Angular también puede transformar valores cambiando su tipo, en este ejemplo transformaría "false" a false y "2" a 2 o
devolveria NaN en caso de fallar la conversión.

````typescript
import {Component, Input, booleanAttribute, numberAttribute} from '@angular/core';

@Component({...})
export class CustomSlider {
    @Input({transform: booleanAttribute}) disabled = false;
    @Input({transform: numberAttribute}) number = 0;
}
````

Para comprobar el tipo de variable:

```typescript
@Component({...})
export class CustomSlider {
    @Input({transform: appendPx}) widthPx: string = '';
}

function appendPx(value: number) {
    return `${value}px`;
}
```

### Inputs con getters y setters

```typescript
export class CustomSlider {
  @Input()
  get value(): number {
    return this.internalValue;
  }
  set value(newValue: number) {
    this.internalValue = newValue;
  }
  private internalValue = 0;
}
```

También se puede declarar un input de solo escritura:

```typescript
export class CustomSlider {
  @Input()
  set value(newValue: number) {
    this.internalValue = newValue;
  }
  private internalValue = 0;
}
```

## Output

Para enviar datos desde un componente hijo a un componente padre se utiliza `@Output`:

```typescript
@Component({...})
export class ExpandablePanel {
  @Output() panelClosed = new EventEmitter<void>();
}
```

```html
<expandable-panel (panelClosed)="savePanelState()" />
```

```typescript
this.panelClosed.emit();
```

Puedes enviar datos llamando a `emit`:

```typescript
// You can emit primitive values.
this.valueChanged.emit(7);
// You can emit custom event objects
this.thumbDropped.emit({
  pointerX: 123,
  pointerY: 456,
})
```

Al definir un detector de eventos en una plantilla, puede acceder a los datos del evento desde la variable $event:

```html
<custom-slider (valueChanged)="logValue($event)" />
```

### Personalizando los nombre de los Outputs
```typescript
@Component({...})
export class CustomSlider {
  @Output('valueChanged') changed = new EventEmitter<number>();
}
```

```html
<custom-slider (valueChanged)="saveVolume()" />
```
