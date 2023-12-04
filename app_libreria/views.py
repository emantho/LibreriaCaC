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
    template_name = "libro_detail.html"

class LibroCreateView(LibroBaseView,CreateView):
    template_name = "libro_create.html"
    extra_context = {
        "tipo": "Crear Libro"
    }


class LibroUpdateView(LibroBaseView,UpdateView):
    template_name = "libro_update.html"
    extra_context = {
        "tipo": "Actualizar Libro"
    }

class LibroDeleteView(LibroBaseView,DeleteView):
    template_name = "libro_delete.html"
    extra_context = {
        "tipo": "Borrar Libro"
    }

