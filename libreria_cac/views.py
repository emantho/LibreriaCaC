from django.views.generic import TemplateView

class IndexPage(TemplateView):
	template_name = "index.html"

class LibrosPage(TemplateView):
	template_name = "libros.html"

class CategoriasPage(TemplateView):
	template_name = "categorias.html"

class CarritoPage(TemplateView):
	template_name = "carrito.html"

class LoginPage(TemplateView):
	template_name = "login.html"

