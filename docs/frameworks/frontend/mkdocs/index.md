# Guía de Configuración de MkDocs

¡Bienvenido a la guía de configuración de MkDocs! Aquí te explicamos cómo iniciar, configurar y personalizar tu proyecto de documentación usando MkDocs.

## Introducción

[MkDocs](https://www.mkdocs.org/) es una herramienta de generación de sitios estáticos que se centra en la creación de documentación de proyectos. Es fácil de configurar y permite generar documentación elegante usando Markdown.

## Características Principales

- **Simplicidad**: Usa Markdown para escribir tus documentos.
- **Temas**: Incluye varios temas atractivos, incluyendo Material Design.
- **Despliegue fácil**: Publica en GitHub Pages, GitLab Pages, o tu servidor preferido.

## Instalación

Para instalar MkDocs, necesitas tener Python y `pip` instalados en tu sistema.

```bash
pip install mkdocs
```

## Verificar la Instalación

Para asegurarte de que MkDocs se ha instalado correctamente, ejecuta el siguiente comando:

```bash
mkdocs --version
```

Deberías ver la versión de MkDocs que has instalado.

## Creación de un Proyecto Nuevo

Para crear un proyecto nuevo, usa el siguiente comando:

```bash
mkdocs new nombre-de-tu-proyecto
```

Esto creará una estructura básica de archivos y carpetas que puedes empezar a personalizar.

## Estructura de Carpetas

Un proyecto típico de MkDocs tendrá la siguiente estructura de carpetas:

```shell
nombre-de-tu-proyecto/
├── docs/
│   └── index.md
└── mkdocs.yml
```

- docs/: Aquí es donde irán todos tus archivos de documentación en formato Markdown.
- mkdocs.yml: Este es el archivo de configuración principal de MkDocs.

## Configuración Básica

El archivo mkdocs.yml es donde configurarás tu sitio de documentación. Aquí un ejemplo básico:

```yaml
site_name: Mi Proyecto
theme:
  name: material

nav:
  - Inicio: index.md
  - Acerca de: about.md
```

## Personalización

Puedes personalizar tu sitio modificando el archivo mkdocs.yml. Algunas opciones comunes incluyen:

- Cambiar el tema: Hay varios temas disponibles que puedes usar.
- Añadir un favicon: Puedes añadir un ícono personalizado a tu sitio.

```yaml
extra:
  favicon: 'img/logo.png'
```

## Desarrollando el Sitio

Durante el desarrollo, puedes usar el servidor de desarrollo integrado de MkDocs para ver los cambios en tiempo real:

```bash
mkdocs serve
```

Esto abrirá un servidor en http://127.0.0.1:8000/ donde podrás ver tu sitio.

## Despliegue del Sitio

Para desplegar tu sitio, primero debes construirlo con el comando:

```bash
mkdocs build
```

Esto generará una carpeta site/ con todos los archivos estáticos de tu sitio. Puedes subir esta carpeta a cualquier servidor o servicio de hosting, como GitHub Pages.

## Ejemplo Completo de mkdocs.yml

Aquí tienes un ejemplo más completo de un archivo mkdocs.yml:

```yaml
site_name: Documentación de Ejemplo

theme:
  name: material
  language: es
  logo: img/logo.png
  favicon: 'img/logo.png'
  features:
    - content.code.copy

nav:
  - Inicio: index.md
  - Guía de Usuario:
      - Instalación: user-guide/installation.md
      - Configuración: user-guide/configuration.md
  - Referencia: reference.md
  - Acerca de: about.md
```
  
## Recursos Adicionales

- [Documentación Oficial de MkDocs](https://www.mkdocs.org/)

- [Tema Material para MkDocs](https://github.com/squidfunk/mkdocs-material)