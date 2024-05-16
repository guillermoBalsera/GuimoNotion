<div align="center">
   <h1>PHP-Laravel</h1>
  <img src="./Logo/logo.png" alt="Descripción de la imagen" width="200px" height="200px">
</div>
   
# 1. Instalación Laravel y creación del proyecto

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

Crear el proyecto (Elegir la opcion 0 o blame) ¿?
```
php artisan breeze: install
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

# 2. Migraciones

Crear migración (Se deben crear en el orden en que se desea que se ejecuten)
```
php artisan:makemigration create_nombre_table
```

Configurar las migraciones
```javascript
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

# 3. Configuración

Hay que modificar el archivo .env (Se encuentra en el directorio raiz):

```javascript
 'mysql' => [
            'driver' => 'mysql',
            'url' => env('DATABASE_URL'),
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '3306'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'unix_socket' => env('DB_SOCKET', ''),
            'charset' => 'utf8mb4',
            'collation' => 'utf8mb4_unicode_ci',
            'prefix' => '',
            'prefix_indexes' => true,
            'strict' => true,
            'engine' => null,
            'options' => extension_loaded('pdo_mysql') ? array_filter([
                PDO::MYSQL_ATTR_SSL_CA => env('MYSQL_ATTR_SSL_CA'),
            ]) : [],
        ],
```

# 4. Modelo

















