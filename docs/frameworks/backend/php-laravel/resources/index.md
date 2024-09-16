# Resources

Los `resources` son herramientas para dar forma a las respuestas _JSON_ de la _API_, de tal manera que nos permiten
personalizar la presentación de los datos.

Para crear un `resource` usaremos el comando:

```
php artisan make:resource NombreResource
```

Puedes personalizar qué campos incluir, renombrarlos y agregar información adicional.

```php
public function toArray($request)
{
    return [
        'id' => $this->id,
        'titulo' => $this->titulo,
        'contenido' => $this->contenido,
        'fecha' => $this->created_at->format('Y-m-d'),
        'clave_foranea' => $this->nombre_tabla,
        'clave_foranea' => $this->nombre_tabla->campo_tabla
    ];
}
```