<div align="center">
   <img src="./0-Assets/logo.png" alt="Descripción de la imagen" width="200px" height="200px">
   <h1>MARKDOWN</h1>
</div>

---

Markdown es un lenguaje de marcado ligero que se utiliza para formatear texto. Es fácil de leer y escribir, y se convierte en HTML de manera sencilla.

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

- Negrita: Envuelve el texto con 2 asteriscos o 2 guiones bajos. `**negrita**` 
- Cursiva: Envuelve el texto con 1 asterisco o un 1 guión bajo. `*cursiva*`
- Negrita y Cursiva: Usa 3 asteriscos o 3 guiones bajos. `***negrita y cursiva***` 

# Listas

Puedes anidar listas utilizando espacios o tabulaciones antes del marcador de la lista.

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

| Lenguaje     | Alias                 | Lenguaje    | Alias                 | Lenguaje   | Alias              |
| ------------ | --------------------- | ----------- | --------------------- | ---------- | ------------------ |
| Bash / Shell | `bash`, `sh`, `shell` | Java        | `java`                | Python     | `python`, `py`     |
| C            | `c`                   | JavaScript  | `javascript`, `js`    | Ruby       | `ruby`, `rb`       |
| C++          | `cpp`, `c++`          | JSON        | `json`                | Rust       | `rust`             |
| C#           | `csharp`, `cs`        | Kotlin      | `kotlin`              | SQL        | `sql`              |
| CSS          | `css`                 | Markdown    | `markdown`, `md`      | Swift      | `swift`            |
| Diff         | `diff`                | Objective-C | `objective-c`, `objc` | TypeScript | `typescript`, `ts` |
| Go           | `go`                  | Perl        | `perl`, `pl`          | XML        | `xml`              |
| HTML         | `html`                | PHP         | `php`                 | YAML       | `yaml`, `yml`      |

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
