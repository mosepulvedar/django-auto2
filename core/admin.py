from django.contrib import admin
from .models import Automovil, Marca

# Register your models here.

class AutomovilAdmin(admin.ModelAdmin):
    #las tuplas con como arreglos pero no se pueden modificar
    list_display = ('patente', 'marca', 'anio', 'modelo')
    search_fields = ['patente', 'modelo']
    list_filter = ('marca',)


admin.site.register(Automovil, AutomovilAdmin)
admin.site.register(Marca)

