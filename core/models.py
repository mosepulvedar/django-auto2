from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Automovil(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Automovil"
        verbose_name_plural = "Automoviles"
        permissions = (
            ("auto_can_add", "puede agregar autos"),
            ("auto_can_delete", "puede eliminar autos"),
            ("auto_can_modify", "puede modifica autos"),
        )
    
    def __str__(self):
        return self.patente