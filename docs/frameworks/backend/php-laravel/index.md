---
tags:
  - Pending review
  - 02/09/2024
---

# PHP-Laravel

## Instalación de Laravel y creación de un nuevo proyecto

### Instalar Laravel

```
composer global require laravel/installer
```

### Actualizar Laravel

```
composer global update laravel/installer
```

### Versión de Laravel

```
laravel -v
```

### Crear el proyecto

```
composer create-project laravel/laravel APi_12
```

### Intalar Breeze

```
composer require laravel/breeze --dev
```

Elegir la opcion `0` o `blame`

```
php artisan breeze:install
```

```
php artisan migrate
```

```
npm install
```

```
npm run dev
```

## Migraciones

### Crear migración

(Se deben crear en el orden en que se desea que se ejecuten)

```
php artisan make:migration create_nombre_table
```

### Configurar las migraciones

```php
Schema::create('users', function (Blueprint $table) {
   $table->id();
   $table->string('name');
});
```

### Migrar

(Se migra por orden alfabético)

```
php artisan migrate
```

!!! note

    Se migra por orden alfabético o por fecha de creación si no se han modificado los nombres de los archivos.

### Deshacer la última migración

```
php artisan migrate:rollback
```

### Deshacer todas las migraciones

```
php artisan migrate:reset
```

### Deshacer todas las migraciones y migrar de nuevo

```
php artisan migrate:fresh
```

### Estado de las migraciones

```
php artisan migrate:status
```

## Configuración

Hay que modificar el archivo `.env` (Se encuentra en el directorio raiz):

```php
DB_CONNECTION=mysql
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=nombreBD*
DB_USERNAME=*
DB_PASSWORD=*
```

## Modelo

### Crear nuevo modelo

```
php artisan make:model Nombre
```

### Especificar el nombre de la tabla en la base de datos

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

### Atributos

```php
protected $fileable = [
   'id',
   'name'
];
```

!!! note

    Se deben especificar también las **foreign keys**

### Relaciones

#### One to One

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

#### One to Many

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

#### Many to Many

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

Para ejecutar la clase `DatabaseSeeder` usaremos el comando:

```
php artisan db:seed
```

## Factories

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

## Resources

Los **resources** son herramientas para dar forma a las respuestas _JSON_ de la _API_, de tal manera que nos permiten
personalizar la presentación de los datos.

Para crear un **resource** usaremos el comando:

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

## Collections

Las **collections** nos permiten transformar colecciones en respuestas _JSON_ estructuradas.

Para crear una **colection** usaremos el comando:

```
php artisan make:resource ArticuloCollection
```

## Controladores

Para crear un **controlador** usaremos el comando:

```
php artisan make:controller NombreApiController --api
```

Nos creará los métodos index, store, show, update y destroy vacios por defecto.

### Validación de campos con request

Para validar campos es recomendable el uso de **request**, que se trata de una clase donde establecemos una serie de
reglas que deben cumplir los campos.

Si deseamos crear un **request** utilizamos el siguiente comando:

```
php artisan make:request CreateNombreRequest
```

Y dentro de la función `rules` personalizamos las reglas de validación:

```php
public function rules()
    {
        return [
            'titulo' => 'required|string|max:255',
            'contenido' => 'required|string',
            // Otras reglas de validación según tus necesidades
        ];
    }
```

Tras esto no necesitariamos validar en el controlador directamente sino que implementariamos el siguiente código:

```php
public function store(CreateNombreRequest $request) {
  return new NombreResource(Nombre::create($request->all()));
}
```

### Validación de campos en el controlador

Para validar campos en el controlador implementamos el siguiente código dentro de nuestra función:

```php
$validator = Validator::make($request->all(), [
  "id" => "required|exists:processes,id",
  "code" => "required|string|max:250",
  "description" => "required",
  "date" => "required",
]);

if ($validator->fails()) {
  return response()->json($validator->errors(), 400);
}
```

El _id_ solo si es necesario comprobarlo si ese objeto existe en la base de datos para una actualización.
