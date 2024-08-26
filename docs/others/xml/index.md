# XML(Extensive Markup Language)

XML (Extensible Markup Language) es un lenguaje de marcado diseñado para almacenar y transportar datos. A diferencia de
HTML, que tiene un conjunto fijo de etiquetas, XML permite a los desarrolladores definir sus propias etiquetas y
estructuras de datos.

## Estructura

Un documento XML tiene una estructura jerárquica basada en etiquetas. Cada etiqueta tiene un nombre y puede contener
texto, otros elementos, o atributos.

- Declaración XML: La primera línea es la declaración XML que define la versión de XML y la codificación de caracteres
  del documento.
- Elementos o Etiquetas: Un elemento puede contener otros elementos (hijos) o texto.
- Atributos: Los atributos proporcionan información adicional sobre los elementos y están definidos dentro de la
  etiqueta de apertura.

## Notas Importantes sobre XML

- Bien Formado vs. Válido: Un documento XML bien formado sigue las reglas sintácticas de XML (por ejemplo, todas las
etiquetas de apertura deben tener una etiqueta de cierre). Un documento XML válido es un documento bien formado que
también cumple con las reglas definidas por un DTD (Document Type Definition) o un esquema XML.
- Sensibilidad a Mayúsculas: XML es sensible a mayúsculas y minúsculas, por lo que <Titulo> y <titulo> se consideran
elementos diferentes.
- Uso de Espacios en Blanco: XML preserva los espacios en blanco, lo cual es útil cuando se desea mantener el formato del
texto.
- Escapado de Caracteres Especiales: Algunos caracteres como <, >, y & tienen que ser escapados usando &lt;, &gt;, y &amp;
respectivamente para evitar conflictos con la sintaxis de XML.

## Ejemplo de XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<biblioteca>
  <libro genero="tecnología">
    <titulo>Introducción a XML</titulo>
    <autor>Juan Pérez</autor>
    <detalles>
      <editorial>Editorial ABC</editorial>
      <publicado>2024</publicado>
    </detalles>
  </libro>
  <libro genero="ciencia">
    <titulo>El Universo</titulo>
    <autor>María López</autor>
    <detalles>
      <editorial>Editorial XYZ</editorial>
      <publicado>2022</publicado>
    </detalles>
  </libro>
</biblioteca>
```