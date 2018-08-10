from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import SignUpForm

def signup(request):
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})