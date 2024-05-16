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



















