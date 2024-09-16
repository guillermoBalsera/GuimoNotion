# Modelo

## Crear nuevo modelo

```
php artisan make:model Nombre
```

La tabla es el plural del nombre del modelo creado, pero a veces no lo detecta bien asi que le cambiamos manualmente el
nombre para que pueda encontrar la tabla.

```php
protected $table = 'tasks_lists';
```

Con la primary key pasa algo parecido. Laravel asume que cada tabla tiene declarado un campo llamado `id`, pero en caso
de que no sea así debemos sobreescribirlo.

```php
protected $primaryKey = 'id';
```

La propiedad `timestamps` nos permite crear los campos `updated_at` y `created_at` en la base de datos de forma
automática en la base de datos.
Estos campos se actualizan automaticamente al ejercer acciones de actualizado o creación de la fila.

```php
public $timestamps = false;
```

## Atributos

```php
protected $fileable = [
   'id',
   'name'
];
```

!!! warning "Importante"

    Se deben especificar también las **foreign keys**

## Relaciones

## One to One

Se debe crear una funcion `hasOne()` en uno de los modelos.

```php
class Libro extends Model {
  public function portada() {
    return $this->hasOne(Portada::class);
  }
}
```

Si se desea hacer la relación bidireccional debe agregarse al otro modelo el metodo `belongsTo()`

```php
class Libro extends Model {
  public function portada() {
    return $this->hasOne(Portada::class);
  }
}
```

## One to Many

Se debe crear la función `hasMany()` en el modelo que posee varios objetos.

```php
class Autor extends Model
{
  public function libros(){
    return $this->hasMany(Libro::class);
  }
}
```

La relación inversa se establece creando la función `belongsTo()` en el otro modelo.

```php
class Libro extends Model {
  public function autor() {
    return $this->belongsTo(Autor::class);
  }
}
```

## Many to Many

En los dos modelos debe definirse el metodo `belongToMany()`

```php
class Libro extends Model {
  public function bibliotecas() {
    return $this->belongsToMany(Biblioteca::class);
  }
}
```

```php
class Biblioteca extends Model {
  public function libros() {
    return $this->belongsToMany(Libro::class);
  }
}
```