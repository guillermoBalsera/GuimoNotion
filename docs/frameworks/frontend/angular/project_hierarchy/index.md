# Estructura del proyecto

La estructura del proyecto es clave para una buena comprensión y un manejo óptimo del proyecto.

Se recomienda seguir la siguiente estructura:

1. `COMPONENTS`: aquí almacenaremos los distintos componentes reutilizables de nuestro proyecto.
2. `LAYOUT`: en este directorio situaremos el componente base de nuestra aplicación, que actuará como la ruta padre de
   los demás componentes.
3. `MODELS`: usaremos esta carpeta para almacenar las interfaces de los objetos de nuestro modelo, tanto los utilizados
   por la propia aplicación como de los datos recibidos por nuestra API en caso de haberla.
4. `PAGES`: se utiliza para almacenar las distintas páginas de nuestro proyecto. Se divide en dos subdirectios:
    - `AUTH`: en el guardaremos todas las páginas correspondientes a la autentificación del usuario.
    - `MAIN`: guardaremos en el las páginas de las funcionalidades principales, aquellas que estén disponibles para el
      usuario una vez iniciada la sesión.
5. `PIPES`: en el guardamos las pipes personalizadas.
6. `SERVICES`: sirve para almacenar los servicios. Se divide en dos subdirectios:
    - `API`: sirve para los métodos que relacionan el proyecto con la API.
    - `PROJECT`: almacena los servicios correspondientes al proyecto en sí.