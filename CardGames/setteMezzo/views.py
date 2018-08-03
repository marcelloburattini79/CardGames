from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Carta, Topic, Post
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

def new_topic(request, pk):

    try:
        carta = Carta.objects.get(id=pk)
    except:
        raise Http404

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            carta=carta,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('carta', pk=carta.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'carta':carta})