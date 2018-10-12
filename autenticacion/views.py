from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def registro(request):

   # if request.POST:
    #    UserCreationForm.save()

    return render(request, 'autenticacion/registro.html', {
        'form':UserCreationForm
    })