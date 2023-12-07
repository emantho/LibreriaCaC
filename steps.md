

>PRIMERA PARTE< 
Contempla la inicialización del venv, ejecución de venv e instalación de django, etc; además crear directorios "templates" y "static". Las configuraciones en settings.py, urls.py y views.py 

>SEGUNDA PARTE<

1rs steps
----------
--Concepto-- 
extra_context = {"comision":"23506"} --> debe llamarse dentro del codigo html usando doble {{}}.
views.py ->> extra_context = {"comision": "23506 🏂"} # Dynamic content insertion using extra_content
html --> <span class="magic-text">Codo a Codo</span><span> Comision {{comision}}



django-admin startapp app_librebria

python3 manage.py makemigrations

python manage.py migrate

Username (leave blank to use 'eder'): librer0
Email address: libreria@mail.com
Password: librer01234

2nd steps
---------
Front-End integration

Must create urls.py (router) and template folder into app_libreria





App creation
- created app_libreria
- created Libro model with the book template
- app_libreria registered in admin.py
- added custom_app.app_libreria
- Inserted line to append it  into installed_apps in setting.py
- Created DB "nuevos_libros"
- Applied makemigrations and migrate
- Created "librer0" superuser
- Two books insertions made in DB from GUI





# STEP2STEP - Python-Django Project and Hosting in Pythonanywhere


## 1st Part ->> Building Project and structure, venv creation and preparation

    Project build up, venv, global project<name> settings, folder creation {static and templates} 


## 2nd Part ->> App creation, Database connection, and crud development

    App creation, Database connection,  and crud

### 2.1. App creation

	Note: use any of these commands
	$ python manage.py startapp app_vino
	or
	$ django-admin startapp app_vino

### 2.1.1 - Create app -->> django-admin startapp app_libreria
	
	This command create a new folder with files inside
	app_libreria
	- Migrations/	->
	- __init__.py	->
	- admin.py	-> Use for model registration
	- apps.py	-> Type of autoincrement use for table
	- models.py 	-> Abstration or estrcuture for the table
	- tests.py	-> Automate test
	- views.py	-> Views to show information

### 2.1.2 - Models.py
	
	Goto models to create the table structure
	
	from django.db import models
	from django.db.models import Model

	# Create your models here.
	class Libro(models.Model):
    	titulo = models.CharField(max_length=100, null=False, blank=False)
    	autor = models.CharField(max_length=100, null=False, blank=False)
    	editorial = models.CharField(max_length=100, null=False, blank=False)
    	precio = models.IntegerField(max_length=10, null=False, blank=False)
    	fecha_publicacion = models.DateField(max_length=100, null=False, blank=False)
    	isbn = models.CharField(max_length=100, null=False, blank=False, primary_key=True)

    	# podemos crear la tabla con un nombre especifico pero se lo tenemos
    	# que indicar directamente en la metaclase
    
    	class Meta:
        db_table = "Nuevos_ingresos"
    
    	def __str__(self):
        	return f"Titulo: {self.titulo} | Autor: {self.autor} | Editorial: {self.editorial} | ISBN: {self.isbn}"

    	def get_fields(self):
        	return [
            		(field.verbose_name, field.value_from_object(self))
            		for field in self.__class__._meta.fields[1:]
        ]
        
### 2.1.2 - Admins.py
	Go to registrer the model 
	
	from django.contrib import admin
	from .models import Libro

	# Register your models here.
	@admin.register(Libro)
	class LibroAdmin(admin.ModelAdmin):
        ...

### 2.1.3 - Insert app configuration into project.settings.py
    
    # Application definition

    CUSTOM_APPS = [
        "app_libreria"
    ]

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    INSTALLED_APPS += CUSTOM_APPS
    
### 2.2 - Migrate model into Database

#### 2.2.1 - Do Makemigration to prepare changes in Database for the created model 
    python manage.py makemigrations

#### 2.2.2 - Do Migrate to apply the changes into Database
    python manage.py migrate
    # This coommand will create the new table into de Database 

#### 2.2.3 - Create superuser
    python manage.py createsuperuser

    user:    librero
    Email:   libreriacac@mail.com
    passw:   librer01234

### 2.3 - Connection with frontEnd

#### 2.3.1 - Create (ROUTER) file urls.py into app_libreria

#### 2.3.2 - Create folder templates into app_libreria
    Inside this we must create the html to view the actions
    
    >> libro.html
 
    {% extends 'base.html' %} {% load static %} {% block content %}

    <main>
        <div">
            <h1>Libros</h1>
            <h2><a href="{% url 'libro:create' %}">Crear un Libro</a></h2>

            {% for libro in libro_list %}
            <div class="list">
                <fieldset>
                    <legend>Titulo: {{libro.titulo}}</legend>
                    <ul>
                        <li>Autor: {{libro.autor}}</li>
                        <li>Editorial: {{libro.editorial}}</li>
                        <li>Precio: {{libro.precio}}</li>
                        <li>Fecha_publicacion: {{libro.fecha_publicacion}}</li>
                        <li>ISBN: {{libro.isbn}}</li>

                    </ul>
                    <span>
                        <label for="">Borrar</label>
                        <a href="{% url 'libro:delete' libro.id %}">❌</a>
                    </span>
                    <span>
                        <label for="">Editar</label>
                        <a href="{% url 'libro:update' libro.id %}">📝</a>
                    </span>
                    <span>
                        <label for="">Detalles</label>
                        <a href="{% url 'libro:detail' libro.id %}">🔍</a>
                    </span>
                </fieldset>
            </div>
            {% endfor %}
            </div>
    </main>

    {% endblock %}


#### 2.3.3 - Create the views for the html
    Inside this file will exist the CRUD {view, detail, create, update and delete}
    ....
    from django.shortcuts import render
    from django.urls import reverse_lazy
    from django.views import View

    from django.views.generic.list import ListView
    from django.views.generic.detail import DetailView
    from django.views.generic.edit import DeleteView, UpdateView, CreateView


    from .models import Libro

    # Create your views here.


    class LibroBaseView(View):
        template_name = 'libro.html'
        model = Libro
        fields = '__all__'
        success_url = reverse_lazy('libro:all')


    class LibroListView(LibroBaseView,ListView):
        """
        ESTO ME PERMITE CREAR UNA VISTA CON LOS LIBROS
        """

    class LibroDetailView(LibroBaseView,DetailView):
        template_name = "Libro_detail.html"

    class LibroCreateView(LibroBaseView,CreateView):
        template_name = "Libro_create.html"
        extra_context = {
            "tipo": "Crear Libro"
        }


    class LibroUpdateView(LibroBaseView,UpdateView):
        template_name = "Libro_create.html"
        extra_context = {
            "tipo": "Actualizar Libro"
        }

    class LibroDeleteView(LibroBaseView,DeleteView):
        template_name = "Libro_delete.html"
        extra_context = {
            "tipo": "Borrar Libro"
    }
    ....

#### 2.3.4 - Create routes in app_library.urls.py
    ....
    from django.contrib import admin
    from django.urls import path , include


    from .views import      LibroListView   \
                        ,   LibroDetailView \
                        ,   LibroCreateView \
                        ,   LibroUpdateView \
                        ,   LibroDeleteView

    app_name = "libro"

    urlpatterns = [
        path("", LibroListView.as_view(), name="all"),
        path("create/", LibroCreateView.as_view(), name="create"),
        path("<int:pk>/detail/", LibroDetailView.as_view(), name="detail"),
        path("<int:pk>/update/", LibroUpdateView.as_view(), name="update"),
        path("<int:pk>/delete/", LibroDeleteView.as_view(), name="delete")

    ]
    ....

#### 2.3.5 - Append the path into project.urls.py (libreria_cac)

    from django.contrib import admin
    from django.urls import path, include

    from .views import IndexPage
    from .views import LibrosPage
    from .views import CategoriasPage
    from .views import CarritoPage
    from .views import LoginPage

    urlpatterns = [
        path('admin/', admin.site.urls),
        path("", IndexPage.as_view(), name="index"),
        path("libros", LibrosPage.as_view(), name="libros"),
        path("categorias/", CategoriasPage.as_view(), name="categorias"),
        path("carrito", CarritoPage.as_view(), name="carrito"),
        path("login", LoginPage.as_view(), name="login"),
        path("libro/", include("app_libreria.urls")),
    ]

#### 2.3.6 - Point the view to the template in index.html (main page or header)
`
    <li class="navegacion-item"><a class="navegacion-a" href="{% url 'libro:all' %}">Novedades</a></li>
`
### 2.4 - Creating views for app
    This task is for the pages or frontend of the actions of CRUD

#### 2.4.1 - Creating libro_create.html
`
    {% extends 'base.html' %} {% load static %} {% block content %}
    <main>
        <div>
            <!-- <h1>CREAR LIBRO</h1> -->
            <form method="post">
                {% csrf_token %}
                <div>{{form.as_div}}</div> <!-- cada campo el form es un div -->
                <input type="submit" value="{{ tipo }}" />
            </form>
            <a href="{% url 'libro:all' %}">Volver al inicio</a>
        </div>
    </main>

    {% endblock %}
`
#### 2.4.2 - Connecting libro.html with libro_create.html
`
    <h2><a href="{% url 'libro:create' %}">Crear un Libro</a></h2>
`

#### 2.4.3 - create libro_delete.html and connect with libro.html
`
    <span>
        <label for="">Borrar</label>
        <a href="{% url 'libro:delete' libro.id %}">❌</a>
    </span>
`
#### 2.4.4 - create libro_update.html and connecting with libro.html
`
    <span>
        <label for="">Editar</label>
        <a href="{% url 'libro:update' libro.id %}">📝</a>
    </span>
`
#### 2.4.4 - create libro_detail.html and connect with libro.html
`
    <span>
        label for="">Detalles</label>
        <a href="{% url 'libro:detail' libro.id %}">🔍</a>
    </span>
`

## 3rd Part

### 3.1 - Create Serializer into app_libreria
    
    from rest_framework.serializers import ModelSerializer
    from .models import Libro

    class LibroSerializer(ModelSerializer):
        class Meta:
            model = Libro
            fields = "__all__"

### 3.2 - Create viewsets.py

    from rest_framework.viewsets import ModelViewSet
    from .models import Libro
    from .serializers import LibroSerializer
    
    class LibroViewSet(ModelViewSet):
        queryset = Libro.objects.all()
        serializer_class = LibroSerializer

### 3.3 - Create router.py

    from rest_framework import routers
    from .viewsets import LibroViewSet

    router = routers.SimpleRouter()

    <!-- #en este caso se le anexa a la ruta de las urls de la app -->
    router.register("api-libro",LibroViewSet)

### 3.4 - Connect with app_libreria.urls.py

    from django.contrib import admin
    from django.urls import path , include
    
    
    from .views import      LibroListView   \
                        ,   LibroDetailView \
                        ,   LibroCreateView \
                        ,   LibroUpdateView \
                        ,   LibroDeleteView 
    
    from .router import router
    
    app_name = "libro"
    
    urlpatterns = [
        path("", LibroListView.as_view(), name="all"),
        path("create/", LibroCreateView.as_view(), name="create"),
        path("<int:pk>/detail/", LibroDetailView.as_view(), name='detail'),
        path("<int:pk>/update/", LibroUpdateView.as_view(), name='update'),
        path("<int:pk>/delete/", LibroDeleteView.as_view(), name='delete')
    
    ]
    
    urlpatterns += router.urls

### 3.5 - Append External_App into project settings.py

    EXTERNALS = [
    "rest_framework"
    ]

## 3rd Part ->> Deploy in PythonAnywhere and Database integration

### 3.1 - 
### 3.2 - 
### 3.3 - 
### 3.4 - 
### 3.5 - 
### 3.6 - Integration with PythonAnywhere Database 

#### 3.6.1 - Create a DataBase in Database page
    Go to Databases > Select MySQL or Postgres depending the need

##### 3.6.1.1 - Create MySQL Credentials
    MySQL user:     emantho
    MySQL password: librer01234

##### 3.6.1.2 - Create Database and password
    Create a new database name: libreria_cac

##### 3.6.1.2 - Start libreria_cac-Database console
    In Databases page goto databases and select emantho$libreria_cac
    
#### 3.6.2 - Integrate Database with project.settings.py
    Add MySQL database information into project.settings.py

    DATABASES = { # Configuration for remote conection to database, comment local to use
        'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'emantho$libreria_cac',
                'USER': 'emantho',
                'PASSWORD': 'librer01234',
                'HOST': 'emantho.mysql.pythonanywhere-services.com',
                'PORT': '3306',
                }
        }

#### 3.6.3 - Styles for api_libros
    Share static globally

##### 3.6.3.1 - Create folder staticfiles in root
    mkdir staticfiles

##### 3.6.3.2 - change in project.setting.py
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [                    # Used this config locally, comment the others
    BASE_DIR / "static"]
    STATIC_ROOT = BASE_DIR / "staticfiles"  # Used this config in PythonAnywhere for API style

##### 3.6.3.3 - Do collectstatic
    python manage.py collectstatic
    and then a *Reload*

### 3.7 - CORS
    Working with remote servers and externals connections

#### 3.7.1 - Create cors.py in app_folder
    mkdir cors.py in app_libreria

#### 3.7.2 - Adding cors configuration in project.settings.py
    CUSTOM_MIDDLEWARE = ["app_libreria.cors.CorsMiddlewareMixin"]
    MIDDLEWARE += CUSTOM_MIDDLEWARE

    