from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Carta

def home(request):
    carte = Carta.objects.all()
    return render(request, 'home.html', {'carte': carte})