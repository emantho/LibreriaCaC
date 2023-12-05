from django.db import models
from django.db.models import Model

# Create your models here.
class Libro(models.Model): # This is the model to be registered in app_libreria.admin.py
    titulo = models.CharField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    editorial = models.CharField(max_length=100, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    fecha_publicacion = models.DateField(max_length=100, null=False, blank=False)
    isbn = models.CharField(max_length=100, null=True, blank=False)

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

