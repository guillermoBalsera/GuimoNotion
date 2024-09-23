---
tags:
  - In development
  - 16/09/2024
---

# PHP-Laravel

## Instalación de Laravel y creación de un nuevo proyecto

### Instalar Laravel

Ejecuta el siguiente comando para instalar Laravel de manera global con Composer:

```
composer global require laravel/installer
```

Si ya tienes instalado el instalador y quieres asegurarte de estar usando la última versión, ejecuta:

```
composer global update laravel/installer
```

Puedes comprobar que Laravel se haya instalado correctamente verificando su versión:

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
