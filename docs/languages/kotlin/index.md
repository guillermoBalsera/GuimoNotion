---
tags:
  - In development
  - Pending review
  - 02/08/204
---

# Kotlin

## Tipos de variables

```kotlin
val numero: Int = 10
val pi: Double = 3.14
val esVerdadero: Boolean = true
val letra: Char = 'A'
val texto: String = "Kotlin es genial!"
```

En Kotlin, puedes declarar variables usando val o var:

- `val`: Inmutable (como final en Java). No se puede reasignar.
- `var`: Mutable. Se puede reasignar.

```kotlin
val nombre = "Juan"  // No puede ser cambiado
var edad = 25        // Puede ser cambiado
```

### Arrays o Listas

```kotlin
val lista = listOf("Manzana", "Banana", "Cereza")
println(lista[1])  // Banana
```

### Sets o conjuntos

```kotlin
val conjunto = setOf(1, 2, 3, 2, 1)
println(conjunto.size)  // 3
```

### Maps o Mapas

```kotlin
val mapa = mapOf(1 to "Uno", 2 to "Dos", 3 to "Tres")
println(mapa[2])  // Dos
```

## Estructuras de Control

### If/Else

```kotlin
val numero = 10

if (numero > 0) {
    println("Número positivo")
} else {
    println("Número negativo")
}
```

### When (Switch)

```kotlin
val dia = 3

val diaSemana = when (dia) {
    1 -> "Lunes"
    2 -> "Martes"
    3 -> "Miércoles"
    4 -> "Jueves"
    5 -> "Viernes"
    6 -> "Sábado"
    7 -> "Domingo"
    else -> "Día no válido"
}

println(diaSemana)
```

### For

```kotlin
for (i in 1..5) {
    println(i)
}
```

### While

```kotlin
var i = 1

while (i <= 5) {
    println(i)
    i++
}
```

## Funciones

Las funciones en Kotlin se declaran con la palabra clave fun:

```kotlin
fun suma(a: Int, b: Int): Int {
    return a + b
}

val resultado = suma(5, 10)
println(resultado)  // 15
```

También puedes definir funciones de una sola línea:

```kotin
fun resta(a: Int, b: Int) = a - b
```

## Clases y Objetos

Kotlin soporta la programación orientada a objetos:

```kotlin
class Persona(val nombre: String, var edad: Int)

val persona = Persona("Juan", 25)
println(persona.nombre)  // Juan
println(persona.edad)    // 25

persona.edad = 26
println(persona.edad)    // 26
```

## Null Safety

Kotlin maneja los valores nulos de manera segura para evitar excepciones de puntero nulo.

```kotlin
var nombre: String? = "Juan"
nombre = null  // Esto es válido

// Uso seguro con null
val longitud = nombre?.length ?: 0
println(longitud)  // 0
```