## Seeders

Los **seeders** sirven para rellenar la base de datos con información inicial.

Para crear un **seeder** usaremos el comando:

```
php artisan make:seeder NombreSeeder
```

Se recomienda crear un **seeder** para cada tabla. En este **seeder** se creará un método `run` donde escribiremos los
datos que queremos introducir en la base de datos.

Desde la función `run` de la clase `DatabaseSeeder` llamaremos a los distintos **seeders**

```php
$this->call(NombreSeeder::class);
```

```php
User::factory()->create([
    'name' => 'Nombre',
    'email' => 'test@example.com',
    'password' => 'test',
    'color_id' => Color::where('name', 'LIKE', 'NARANJA')
]);
```

Para ejecutar la clase `DatabaseSeeder` usaremos el comando:

```
php artisan db:seed
```