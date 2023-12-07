# libreria_cac
Proyecto final del Curso Full Stack Python y entregable del Backend con Django

Este proyecto Django tiene como objetivo proporcionar una solución simple y eficaz para gestionar el inventario de libros de una biblioteca. La estructura del proyecto incluye la aplicación principal de Django, archivos estáticos para estilos y scripts, y plantillas HTML para representar páginas.


## FRONTEND { HTML, CSS, JAVASCRIPT}
## BACKEND {PYTHON, DJANGO, SQLITE3 / MySQL}

## integrantes 
* Eder Manjarres
* Julio
*


## Estructura de proyecto
```
.
├── app_libreria
│   ├── admin.py
│   ├── apps.py
│   ├── cors.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_libro_isbn.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0002_alter_libro_isbn.cpython-310.pyc
│   │       ├── 0002_alter_libro_precio.cpython-310.pyc
│   │       ├── 0003_alter_libro_table.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── cors.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── router.cpython-310.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── views.cpython-310.pyc
│   │   └── viewsets.cpython-310.pyc
│   ├── router.py
│   ├── serializers.py
│   ├── templates
│   │   ├── libro_create.html
│   │   ├── libro_delete.html
│   │   ├── libro_detail.html
│   │   └── libro.html
│   ├── tests.py
│   ├── urls.py
│   ├── viewsets.py
│   └── views.py
├── db.sqlite3
├── libreria_cac
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── views.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── LICENSE
├── manage.py
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   └── style.css
│   ├── icon
│   │   ├── icons8-book-48.ico
│   │   ├── icons8-facebook-50.ico
│   │   ├── icons8-instagram-50.ico
│   │   └── icons8-youtube-50.ico
│   ├── image
│   │   ├── 73-margaritas.jpg
│   │   ├── amazonia.jpg
│   │   ├── apia-de-roma.jpg
│   │   ├── apologia-de-socrates.jpeg
│   │   ├── aprender-a-ser-salvajes.jpg
│   │   ├── artificial.jpg
│   │   ├── bowie.jpeg
│   │   ├── buenos-aires.jpg
│   │   ├── calculus.jpg
│   │   ├── derecho-internacional-privado.jpg
│   │   ├── diagnostico-de-la-personalidad.jpg
│   │   ├── el-amor-es-imposible.jpg
│   │   ├── el-buddhismo.jpg
│   │   ├── el-cerebro-del-artista.jpg
│   │   ├── el-corazon-del-hombre.jpg
│   │   ├── el-ejercito-del-amanecer.jpg
│   │   ├── el-escondite.jpg
│   │   ├── el-golem.jpg
│   │   ├── el-hombre-en-busca-de-sentido.jpg
│   │   ├── el-portador-de-la-luz.jpg
│   │   ├── el-principio-de-proporcionalidad.jpg
│   │   ├── el-problema-final.jpg
│   │   ├── el-vuelo-de-la-libelula.jpg
│   │   ├── fedon.jpg
│   │   ├── fisica-general.jpg
│   │   ├── holly-edicion-en-espanol.jpg
│   │   ├── horoscopo-chino-2024.jpg
│   │   ├── icons8-book-48.png
│   │   ├── icons8-facebook-50.png
│   │   ├── icons8-instagram-50.png
│   │   ├── icons8-shopping-cart-48.png
│   │   ├── icons8-youtube-50.png
│   │   ├── la-armadura-de-la-luz-saga-los-pilares-de-la-tierra-4.jpg
│   │   ├── la-llamada-de-cthulhu.jpeg
│   │   ├── la-musica-en-cuba.jpg
│   │   ├── la-sangre-manda.jpg
│   │   ├── las-invitadas-secretas.jpeg
│   │   ├── lofts.jpg
│   │   ├── los-adversarios.jpg
│   │   ├── luxury.jpg
│   │   ├── materials.jpg
│   │   ├── meditaciones.jpg
│   │   ├── metropolis.jpg
│   │   ├── mexico.jpg
│   │   ├── mitos-populares-de-japon.jpg
│   │   ├── oxido.jpg
│   │   ├── peter-pan-y-wendy.jpeg
│   │   ├── precisiones.jpg
│   │   ├── quimica-inorganica.jpg
│   │   ├── roger-waters.jpg
│   │   ├── susan-q-yin-2JIvboGLeho-unsplash.jpg
│   │   ├── taylor-from-the-vault.jpg
│   │   ├── tom-hermans-9BoqXzEeQqM-unsplash.jpg
│   │   ├── ugur-akdemir-XT-o5O458as-unsplash.jpg
│   │   ├── una-venganza-para-mi-enemigo.jpg
│   │   ├── un-mundo-de-ensueno.jpg
│   │   └── vidas-sorprendentes.jpg
│   └── js
│       ├── carrito.js
│       ├── categorias.js
│       ├── colapsable.js
│       ├── compararContrasenia.js
│       ├── dropdown.js
│       ├── libros.js
│       ├── sliderIngresosRecomendados.js
│       ├── validarFormContacto.js
│       └── validarUsuario.js
├── staticfiles
│   ├── admin
│   │   ├── css
│   │   │   └── vendor
│   │   │       └── select2
│   │   ├── img
│   │   │   └── gis
│   │   └── js
│   │       ├── admin
│   │       └── vendor
│   │           ├── jquery
│   │           ├── select2
│   │           │   └── i18n
│   │           └── xregexp
│   ├── css
│   ├── icon
│   ├── image
│   ├── js
│   └── rest_framework
│       ├── css
│       ├── docs
│       │   ├── css
│       │   ├── img
│       │   └── js
│       ├── fonts
│       ├── img
│       └── js
├── steps.md
└── templates
    ├── base.html
    ├── carrito.html
    ├── categorias.html
    ├── index.html
    ├── login.html
    └── partials
        ├── footer.html
        └── header.html
```
## Aplicación Libreria Codo a Codo

...
La aplicación Librería habilitará la gestión de libros, permitiendo la creación, edición, visualización y eliminación de estos. 

Se habilitarán una vista de administración con acceso total a las funciones de la aplicación. 

## Estructura del CRUD usado

### Aplicación Libreria app_libreria
```
├──app_libreria
    ├── libro_create.html
    ├── libro_delete.html
    ├── libro_detail.html
    └── libro.html
```
***libro.html*** -> Es la vista principal de la app es donde se listan los libros creados; cada libro cuenta con botones para ejecutar las acciones siguientes:
* **libro_create** -> Abre una vista con un formulario con los campos de caracteristicas del libro
* **libro_detail** -> Abre una vista listando los detalles del libro
* **libro_delete** -> Borra el libro seleccionado
* ***La edición*** se hace utilizando libro_create + el id del libro, lo que permite editar los campos

## API Routes Documentation

### Method: GET,PUT, DELETE
URL: /api/api-libro/<id>/
Description: Retrieves, updates, or deletes a specific libro by ID.
Headers: Content-Type': 'application/json

### Method: POST
URL: /api/api-libro
Description: Generates a new libro.
Headers: Content-Type: application/json"
Body: {
    "titulo": "",
    "autor": "",
    "editorial":"",
    "precio":,
    "fecha_publicacion":"",
    "isbn":""
    }

## Admin
### Admin Panel
Method: GET
URL: /admin/
Description: Access to Django admin panel for administration purposes.

