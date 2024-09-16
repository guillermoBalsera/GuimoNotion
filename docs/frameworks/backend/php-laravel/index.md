---
tags:
  - Pending review
  - 16/09/2024
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

Elegir la opcion `0` o `blade`

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
