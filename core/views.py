from django.shortcuts import render
from .models import Automovil, Marca
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
def home(request):
    return render(request, 'core/home.html')


def galeria(request):
    return render(request, 'core/galeria.html')

def listar_automovil(request):
    #obtenemos todos los automoviles desde la BBDD
    autos = Automovil.objects.all()
    #le pasamos los automoviles al template
    #para que el los despliegue
    return render(request, 'core/listado_automoviles.html',{
        'autos':autos
    })


@permission_required('core.auto_can_add')
def formulario_automovil(request):

    marcas = Marca.objects.all()
    #declaramos las variables que se enviarán al template
    variables = {
        'marcas':marcas
    }
    #preguntamos si la peticion es POST, lo que quiere decir que el usuario
    #presiono el boton en el formulario
    if request.POST:
        #instanciamos un modelo Automovil
        auto = Automovil()
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = int(request.POST.get('txtAnio'))
        #instanciar un modelo Marca
        marca = Marca()
        marca.id = int(request.POST.get('cboMarca'))
        #le pasamos el modelo Marca al Automovil
        auto.marca = marca
        try:
            auto.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

        
    return render(request, 'core/formulario_automovil.html', variables)

