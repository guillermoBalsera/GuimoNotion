# Migraciones

## Crear migración

(Se deben crear en el orden en que se desea que se ejecuten)

```
php artisan make:migration create_nombre_table
```

## Configurar las migraciones

```php
Schema::create('users', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->date('birth_date')->nullable();
    $table->enum('gender', ['Male', 'Female']);
    $table->foreign('address_id')->references('id')->on('addresses')->onDelete('cascade');
    $table->timestamps();
});

public function down(): void {
    Schema::dropIfExists('breedings');
}
```

## Migrar

(Se migra por orden alfabético)

```
php artisan migrate
```

!!! note "Orden de las migraciones"

    Se migra por orden alfabético o por fecha de creación si no se han modificado los nombres de los archivos.

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