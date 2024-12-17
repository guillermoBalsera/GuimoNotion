# Variables de entorno

## Públicas

Con variables de entorno públicas nos referimos a todas aquellas que **no** sean sensibles, como URLs, nombres de servicios
o configuraciones.

Para este tipo de variables usamos los `environments`:

```shell
ng generate environments
```

Este comando generará dos archivos: `environment.ts` para producción y `environment.development.ts` para desarrollo.

Ahora debemos añadir las variables en ambos archivos:

```typescript
export const environment = {
  apiUrl: 'http://localhost:3000',
};
```

Se importa el archivo environment y ya se pueden usar las variables:

```typescript
import { environment } from '../environments/environment';

const apiUrl = environment.apiUrl;
```

Después debemos editar la configuración para que se cambie automáticamente al construir nuestra aplicación en el archivo `angular.json`:

```json
"configurations": {
            "production": {
              ...
              "fileReplacements": [
                {
                  "replace": "src/environments/environment.development.ts",
                  "with": "src/environments/environment.ts"
                }
              ]
            },
            "development": {
              ...
              "fileReplacements": [
                {
                  "replace": "src/environments/environment.ts",
                  "with": "src/environments/environment.development.ts"
                }
              ]
            }
          } 
```

A la hora de construir nuestra aplicación para producción es importante especificar si estamos construyendo producción o desarrollo:

```shell
ng build --configuration production # development
```
