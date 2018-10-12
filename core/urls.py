from django.urls import path
from .views import home, galeria,listar_automovil,formulario_automovil

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('automoviles/', listar_automovil, name="automoviles"),
    path('formulario-auto/', formulario_automovil, name="formulario_auto"),
]

