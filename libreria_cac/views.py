from django.views.generic import TemplateView

class IndexPage(TemplateView):
	template_name = "index.html"
 
class CategoriaPage(TemplateView):
	template_name = "categorias.html"

class CarritoPage(TemplateView):
	template_name = "carrito.html"

class LoginPage(TemplateView):
	template_name = "login.html"


