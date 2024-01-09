from django.shortcuts import render, redirect
from .models import Accion

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        acciones = Accion.objects.filter(users=request.user)
        return render(request, 'home.html', {"acciones":acciones})
    else:
        return redirect('login')