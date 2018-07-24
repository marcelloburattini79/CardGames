from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Carta

def home(request):

    carte = Carta.objects.all()

    return render(request, 'home.html', {'carte': carte})

def carta_dett(request, pk):

    carta = Carta.objects.get(id=pk)

    return render(request, 'carta_dett.html', {'carta': carta})