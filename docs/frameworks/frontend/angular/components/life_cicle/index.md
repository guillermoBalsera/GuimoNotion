# Ciclos de vida de un componente

=== "Creación"

    | Método        | Resumen                                                                                                                                                                           |
    |---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `constructor` | Se ejecuta cuando Angular instancia el componente. Aquí se deben inicializar propiedades, pero no es recomendable realizar operaciones complejas que dependan del DOM o de datos. |

=== "Cambio"

    | Método                  | Resumen                                                                                                                         |
    |-------------------------|---------------------------------------------------------------------------------------------------------------------------------|
    | `ngOnInit`              | Se ejecuta una vez después de que Angular ha inicializado todos los inputs del componente. Ideal para inicializar datos.        |
    | `ngOnChanges`           | Se ejecuta cada vez que hay un cambio en los inputs de un componente (cuando un valor vinculado a `@Input` cambia).             |
    | `ngDoCheck`             | Se ejecuta durante cada ciclo de detección de cambios, permitiendo la implementación de una detección de cambios personalizada. |
    | `ngAfterContentInit`    | Se ejecuta después de que Angular haya proyectado contenido externo dentro del componente (solo una vez).                       |
    | `ngAfterContentChecked` | Se ejecuta después de que Angular haya verificado los cambios en el contenido proyectado en el componente.                      |
    | `ngAfterViewInit`       | Se ejecuta después de que Angular inicialice las vistas del componente y sus vistas secundarias (solo una vez).                 |
    | `ngAfterViewChecked`    | Se ejecuta después de que Angular verifique los cambios en las vistas del componente y sus vistas secundarias.                  |

=== "Renderizado"

    | Método            | Resumen                                                                     |
    |-------------------|-----------------------------------------------------------------------------|
    | `afterNextRender` | Se ejecuta la próxima vez que todos los componentes hayan sido renderizados |
    | `afterRender`     | Se ejecuta cada vez que todos los componentes hayan sido renderizados       |

=== "Destrucción"

    | Método        | Resumen                                                                                                                                                           |
    |---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `ngOnDestroy` | Se ejecuta justo antes de que Angular destruya el componente. Ideal para liberar recursos, cancelar suscripciones, o eliminar listeners para evitar memory leaks. |

## ngOnChanges

El método `ngOnChanges` acepta el argumento `SimpleChanges`. Este objeto es un registro de cada uno de
los `SimpleChange`. Cada uno de estos contiene el valor previo del `@Input`, su valor actual y un indicador de si esta
es la primera vez que cambia.

```typescript
@Component({
    /* ... */
})
export class UserProfile {
    @Input() name: string = '';

    ngOnChanges(changes: SimpleChanges) {
        for (const inputName in changes) {
            const inputValues = changes[inputName];
            console.log(`Previous ${inputName} == ${inputValues.previousValue}`);
            console.log(`Current ${inputName} == ${inputValues.currentValue}`);
            console.log(`Is first ${inputName} change == ${inputValues.firstChange}`);
        }
    }
}
```

## DestroyRef

Como una alternativa a `ngOnDestroy` puedes inyectar una instancia de `DestroyRef`. Puedes registrar una devolución de
llamada para que se invoque tras la destrucción del componente llamando al método `onDestroy` de `DestryRef`.

```typescript
@Component({
    /* ... */
})
export class UserProfile {
    constructor(private destroyRef: DestroyRef) {
        destroyRef.onDestroy(() => {
            console.log('UserProfile destruction');
        });
    }
}
```

!!! note

    Puede pasar la DestroyRef instancia a funciones o clases externas a su componente. Utilice este patrón si tiene otro
    código que debería ejecutar algún comportamiento de limpieza cuando se destruye el componente.
