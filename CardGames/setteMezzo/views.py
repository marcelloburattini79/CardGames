from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Carta
from django.http import Http404

def home(request):

    carte = Carta.objects.all()

    return render(request, 'home.html', {'carte': carte})

def carta_dett(request, pk):

    try:
        carta = Carta.objects.get(id=pk)
    except:
        raise Http404

    return render(request, 'carta_dett.html', {'carta': carta})