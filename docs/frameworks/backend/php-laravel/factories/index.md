# Factories

Los **factories** son clases que crean por nosotros datos ficticios automáticamente.

Para crear un **factorie** usaremos el comando:

```
php artisan make:factorie NombreFactorie
```

Se recomienda crear un **factorie** para cada clase.

En este **factorie** debemos completar el atributo `model` y la función `definition()`.

```php
class NombreFactory extendes Factory {
  protected $model = Nombre::class;

  public function definition() {
    return [
      'atributo' => fake()->name(),
      'atributo' => fake()->name(),
      'foreign_key' => ModeloForeignKey::all()->random()->id,
    ];
  }
}
```

Desde la función `run` de la clase **Seeder** podemos llamar al **factorie** de la siguiente forma:

```php
\App\Models\Nombre::factory(número)->create();
```