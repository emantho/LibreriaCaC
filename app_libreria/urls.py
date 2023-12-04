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