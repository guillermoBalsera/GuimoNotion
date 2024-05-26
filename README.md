<div align="center">
   <img src="./0-Assets/logo.png" alt="Descripción de la imagen" width="200px" height="200px">
   <h1>MARKDOWN</h1>
</div>

---

Markdown es un lenguaje de marcado ligero que se utiliza para formatear texto. Es fácil de leer y escribir, y se convierte en HTML de manera sencilla. A continuación, te presentamos una guía completa sobre cómo usar Markdown.

- [Encabezados](#encabezados)
- [Énfasis](#énfasis)
- [Listas](#listas)
  - [Listas ordenadas](#listas-ordenadas)
  - [Listas desordenadas](#listas-desordenadas)
- [Enlaces](#enlaces)
- [Citas](#citas)
- [Tablas](#tablas)
- [Código](#código)
  - [Código en Línea](#código-en-línea)
  - [Bloques de Código](#bloques-de-código)
  - [Lenguajes](#lenguajes)
- [Líneas horizontales](#líneas-horizontales)
- [Escapando caracteres](#escapando-caracteres)

# Encabezados

Puedes crear encabezados utilizando el símbolo `#`. El número de `#` indica el nivel del encabezado.

```markdown
# Encabezado 1

## Encabezado 2

### Encabezado 3

#### Encabezado 4

##### Encabezado 5

###### Encabezado 6
```

# Énfasis

Puedes agregar énfasis al texto utilizando asteriscos \* o guiones bajos \_.

- Negrita: Envuelve el texto con dos asteriscos \*\* o dos guiones bajos \_\_.
- Cursiva: Envuelve el texto con un asterisco \* o un guión bajo \_.
- Negrita y Cursiva: Usa tres asteriscos \*\*\* o tres guiones bajos \_\_\_.

# Listas

## Listas ordenadas

Utiliza números seguidos de un punto para crear listas ordenadas.

```markdown
1. Primer ítem
2. Segundo ítem
3. Tercer ítem
```

## Listas desordenadas

Utiliza asteriscos \*, signos más + o guiones - para listas desordenadas.

```markdown
- Primer ítem
- Segundo ítem
- Tercer ítem
```

# Enlaces

Puedes crear enlaces utilizando corchetes [] para el texto del enlace y paréntesis () para la URL.

```markdown
[Texto del enlace](https://www.ejemplo.com)
```

# Citas

Para crear citas, utiliza el símbolo >.

```markdown
> Esta es una cita.
```

# Tablas

Puedes crear tablas utilizando guiones - para la línea de encabezado y barras verticales | para separar columnas.

```markdown
| Encabezado 1  | Encabezado 2  |
| ------------- | ------------- |
| Fila 1, Col 1 | Fila 1, Col 2 |
| Fila 2, Col 1 | Fila 2, Col 2 |
```

# Código

## Código en Línea

Para código en línea, usa comillas simples invertidas `.

```markdown
Este es un ejemplo de `código en línea`.
```

## Bloques de Código

Para bloques de código, utiliza tres comillas simples invertidas ``` antes y después del código. Puedes especificar el lenguaje de programación para resaltado de sintaxis.

````markdown
```java
System.out.println("Hola mund0");
```
````

> Para mostrar un bloque de código de markdown dentro de un bloque de código simplemnete se usan mas comillas simples invertidas en el bloque de código externo.

## Lenguajes

En la siguiente tabla se muestra una lista de lenguajes de progración admitidos por Linguistic, el sistema de resaltado de código de GitHub:

<div style="display: flex; justify-content: center;">

| Lenguaje     | Alias                 | Lenguaje    | Alias                 |
| ------------ | --------------------- | ----------- | --------------------- |
| Bash / Shell | `bash`, `sh`, `shell` | Java        | `java`                |
| C            | `c`                   | JavaScript  | `javascript`, `js`    |
| C++          | `cpp`, `c++`          | JSON        | `json`                |
| C#           | `csharp`, `cs`        | Kotlin      | `kotlin`              |
| CSS          | `css`                 | Markdown    | `markdown`, `md`      |
| Diff         | `diff`                | Objective-C | `objective-c`, `objc` |
| Go           | `go`                  | Perl        | `perl`, `pl`          |
| HTML         | `html`                | PHP         | `php`                 |
| Python       | `python`, `py`        | Ruby        | `ruby`, `rb`          |
| Rust         | `rust`                | SQL         | `sql`                 |
| Swift        | `swift`               | TypeScript  | `typescript`, `ts`    |
| XML          | `xml`                 | YAML        | `yaml`, `yml`         |

</div>

# Líneas horizontales

Para agregar una línea horizontal, utiliza tres o más guiones, asteriscos, o guiones bajos.

```markdown
---
```

# Escapando caracteres

Si necesitas usar un carácter especial literalmente, escápalo con una barra invertida \.

```markdown
\*Este texto no estará en cursiva\*
```
