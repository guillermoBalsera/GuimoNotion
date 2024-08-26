# YAML (YAML Ain't Markup Language)

YAML es un formato de serialización de datos muy legible y fácil de escribir, especialmente útil para archivos de
configuración. La indentación es crucial en YAML, ya que define la estructura jerárquica de los datos. Asegúrate de usar
siempre espacios y no tabulaciones para evitar errores de sintaxis.

## Estructura

- Comentarios: comienzan con `#`
- Objetos (mapas): utilizan el formato `clave: valor`
- Anidación: a indentación (espacios) define la jerarquía y la anidación de los datos.
- Listas (Arrays): Se indican con guiones (-) y se pueden anidar dentro de otros objetos.
- Valores en lista sin clave-valor: Las listas también pueden contener valores simples sin formato de clave-valor.

## Ejemplo de YAML

```yaml
# Información básica de una persona
persona:
  nombre: Juan Pérez
  edad: 30
  direccion:
    calle: "123 Calle Principal"
    ciudad: "Ciudad Ejemplo"
    pais: "País de Ejemplo"
  telefonos:
    - tipo: "casa"
      numero: "123-456-7890"
    - tipo: "trabajo"
      numero: "098-765-4321"
  habilidades:
    - programación
    - escritura
    - cocina
```
