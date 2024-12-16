# Editar el menú contextual

Para cambiar el menú que aparece al hacer click derecho en tu página web hecha con Angular, puedes sobreescribir el
comportamiento predeterminado del evento contextmenu y mostrar un menú personalizado

## Interceptar el evento `contextmenu`

En el componente donde desees modificar el menú:

```typescript
import {Component, HostListener} from '@angular/core';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrl: './app.component.css'
})
export class AppComponent {
    showContextMenu = false;
    contextMenuPosition = {x: '0px', y: '0px'};

    @HostListener('document:click')
    onDocumentClick(): void {
        this.showContextMenu = false; //Oculta el menú al hacer click fuera
    }

    onRightClick(event: MouseEvent): void {
        event.preventDefault(); // Evita que aparezca el menú por defecto
        this.showContextMenu = true;
        this.contextMenuPosition = {
            x: `${event.clientX}px`,
            y: `${event.clientY}px`
        }
    }

    hendleOption(option: string): void {
        console.log(`Opción seleccionada ${option}`);
        this.showContextMenu = false;
    }
}
```

## Modificar el HTML

```html

<div (contextmenu)="onRightClick($event)">
    <p>Haz click derecho aquí</p>
</div>

<div *ngIF="showContextMenu" [ngStyle]="{ top: contextMenuPosition.y, left: contextMenuPosition.x }"
     class="context-menu">
    <ul>
        <li click="handleOption('option1')">Opción 1</li>
        <li click="handleOption('option2')">Opción 2</li>
        <li click="handleOption('option3')">Opción 3</li>
    </ul>
</div>
```