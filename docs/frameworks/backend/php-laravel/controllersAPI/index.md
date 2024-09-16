# Controladores

Para crear un **controlador** usaremos el comando:

```
php artisan make:controller NombreApiController --api
```

Nos creará los métodos index, store, show, update y destroy vacios por defecto.

## Validación de campos en el controlador

Para validar campos en el controlador implementamos el siguiente código dentro de nuestra función:

```php
$validator = Validator::make($request->all(), [
  "id" => "required|exists:processes,id",
  "code" => "required|string|max:250",
  "description" => "nullable",
  "date" => "required",
  "gender" => "in:Male,Female"
]);

if ($validator->fails()) {
  return response()->json($validator->errors(), 400);
}
```

## Ejemplos

### Index

```php
public function index()
{
    $users = User::all();
    return $users;
}
```

En `Laravel` viene implementada una función de paginación por defecto:

```php
public function index()
{
    $users = User::paginate($nResults);
    return $users;
}
```

### Show

```php
public function show($id)
{
    $user = User::findOrFail($id);
    return $user;
}
```

### Store

```php
public function store(Request $request)
{
    $user = User::create($request);
    return $user;
}
```

### Update

```php
public function update(Request $request, $id)
{
    $user = User::findOrFail($id);
    $user->update([
        'dni' => $request->input('dni')
       ]);
    return $user;
}
```

El _id_ solo si es necesario comprobarlo si ese objeto existe en la base de datos para una actualización.
