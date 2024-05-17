<div align="center">
   <img src="./Logo/logo.png" alt="Descripción de la imagen" width="200px" height="200px">
   <h1>PHP-Laravel</h1>
</div>

# Proyecto Ejemplo

## Índice
- [Introducción](#introducción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Introducción
Aquí va la introducción de tu proyecto.

## Instalación
Instrucciones para instalar tu proyecto.

## Uso
Ejemplos y guías de uso.

## Contribuir
Guía para contribuir al proyecto.

## Licencia
Información sobre la licencia del proyecto.

   
## 1. Instalación de Laravel y creación de un nuevo proyecto

Instalar Laravel
```
composer global require laravel/installer
```

Actualizar Laravel
```
composer global update laravel/installer
```

Versión de Laravel
```
laravel -v
```

Intalar Breeze
```
composer require laravel/breeze --dev
```

Crear el proyecto ¿?
```
composer create-project laravel/laravel APi_12
```

Elegir la opcion 0 o blame

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

Crear migración (Se deben crear en el orden en que se desea que se ejecuten)
```
php artisan:makemigration create_nombre_table
```

Configurar las migraciones
```php
 Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
 });
```

Migrar (Se migra por orden alfabético)
```
php artisan migrate
```

Deshacer la última migración
```
php artisan migrate:rollback
```

Deshacer todas las migraciones
```
php artisan migrate:reset
```

Deshacer todas las migraciones y migrar de nuevo
```
php artisan migrate:fresh
```

Estado de las migraciones
```
php artisan migrate:status
```

## 3. Configuración

Hay que modificar el archivo .env (Se encuentra en el directorio raiz):

```javascript
DB_CONNECTION=mysql
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=nombreBD*
DB_USERNAME=*
DB_PASSWORD=*
```

## 4. Modelo

Especificar el nombre de la tabla en la base de datos

```php
protected $table = 'tasks_lists';
protected $primaryKey = 'id';
```

### 4.1 Atributos

Se deben especificar también las foreign keys

```php
protected $fileable = [
      'id',
      'name'
    ];
```

### 4.2 Relaciones

#### 4.2.1 One to One


#### 4.2.2 One to Many


#### 4.2.3 Many to Many















