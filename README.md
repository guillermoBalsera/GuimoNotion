<div align="center">
   <img src="./Logo/logo.png" alt="Descripción de la imagen" width="200px" height="200px">
   <h1>PHP-Laravel</h1>
</div>

- [1. Instalación de Laravel y creación de un nuevo proyecto](#1-instalación-de-laravel-y-creación-de-un-nuevo-proyecto)
  - [Instalar Laravel](#instalar-laravel)
  - [Actualizar Laravel](#actualizar-laravel)
  - [Versión de Laravel](#versión-de-laravel)
  - [Instalar Breeze](#instalar-breeze)
  - [Crear el proyecto](#crear-el-proyecto)
  - [Ejecutar comandos iniciales](#ejecutar-comandos-iniciales)
- [2. Migraciones](#2-migraciones)
  - [Crear migración](#crear-migración)
  - [Configurar las migraciones](#configurar-las-migraciones)
  - [Migrar](#migrar)
  - [Deshacer la última migración](#deshacer-la-última-migración)
  - [Deshacer todas las migraciones](#deshacer-todas-las-migraciones)
  - [Deshacer todas las migraciones y migrar de nuevo](#deshacer-todas-las-migraciones-y-migrar-de-nuevo)
  - [Estado de las migraciones](#estado-de-las-migraciones)
- [3. Configuración](#3-configuración)
- [4. Modelo](#4-modelo)
  - [4.1 Atributos](#41-atributos)
  - [4.2 Relaciones](#42-relaciones)
    - [4.2.1 One to One](#421-one-to-one)
    - [4.2.2 One to Many](#422-one-to-many)
    - [4.2.3 Many to Many](#423-many-to-many)
   
## 1. Instalación de Laravel y creación de un nuevo proyecto

##### Instalar Laravel
```
composer global require laravel/installer
```

##### Actualizar Laravel
```
composer global update laravel/installer
```

##### Versión de Laravel
```
laravel -v
```

##### Intalar Breeze
```
composer require laravel/breeze --dev
```

##### Crear el proyecto ¿?
```
composer create-project laravel/laravel APi_12
```

##### Elegir la opcion 0 o blame
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

## 2. Migraciones

##### Crear migración (Se deben crear en el orden en que se desea que se ejecuten)
```
php artisan:makemigration create_nombre_table
```

##### Configurar las migraciones
```php
Schema::create('users', function (Blueprint $table) {
   $table->id();
   $table->string('name');
});
```

##### Migrar (Se migra por orden alfabético)
```
php artisan migrate
```

##### Deshacer la última migración
```
php artisan migrate:rollback
```

##### Deshacer todas las migraciones
```
php artisan migrate:reset
```

##### Deshacer todas las migraciones y migrar de nuevo
```
php artisan migrate:fresh
```

##### Estado de las migraciones
```
php artisan migrate:status
```

## 3. Configuración

##### Hay que modificar el archivo .env (Se encuentra en el directorio raiz):

```javascript
DB_CONNECTION=mysql
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=nombreBD*
DB_USERNAME=*
DB_PASSWORD=*
```

## 4. Modelo

##### Crear nuevo modelo
```
php artisan make:model Nombre
```

##### Especificar el nombre de la tabla en la base de datos

La tabla es el plural del nombre del modelo creado, pero a veces no lo detecta bien asi que le cambiamos manualmente el nombre para que pueda encontrar la tabla.
```php
protected $table = 'tasks_lists';
```

Con la primary key pasa algo parecido. Laravel asume que cada tabla tiene declarado un campo llamado 'id', pero en caso de que no sea así debemos sobreescribirlo.
```php
protected $primaryKey = 'id';
```

La propiedad 'timestamps' nos permite crear los campos 'updated_at' y 'created_at' en la base de datos de forma automática en la base de datos.
Estos campos se actualizan automaticamente al ejercer acciones de actualizado o creación de la fila.
```php
public $timestamps = false;
```

### 4.1 Atributos

```php
protected $fileable = [
   'id',
   'name'
];
```
<small>Se deben especificar también las foreign keys</small>

### 4.2 Relaciones

#### 4.2.1 One to One

Se debe crear una funcion 'hasOne()' en uno de los modelos.

```php
class Libro extends Model {
  public function portada() {
    return $this->hasOne(Portada::class);
  }
}
```

Si se desea hacer la relación bidireccional debe agregarse al otro modelo el metodo 'belongsTo()'

```php
class Libro extends Model {
  public function portada() {
    return $this->hasOne(Portada::class);
  }
}
```

#### 4.2.2 One to Many

Se debe crear la función 'hasMany()' en el modelo que posee varios objetos.

```php
class Autor extends Model
{
  public function libros(){
    return $this->hasMany(Libro::class);
  }
}
```

La relación inversa se establece creando la función 'belongsTo()' en el otro modelo.

```php
class Libro extends Model {
  public function autor() {
    return $this->belongsTo(Autor::class);
  }
}
```

#### 4.2.3 Many to Many

En los dos modelos debe definirse el metodo 'belongToMany()'

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














