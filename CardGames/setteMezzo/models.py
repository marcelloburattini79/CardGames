from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class seme(models.Model):

    value = models.IntegerField("Valore")

    colore = models.CharField(max_length=50)

    def __str__(self):
        return self.colore


class Carta(models.Model):

    value = models.IntegerField("Valore")

    tipo = models.ForeignKey(seme, on_delete = models.CASCADE, related_name='carta')

    def __str__(self):

        return "%s %s" %(self.value, self.tipo)


class Topic(models.Model):

    subject = models.CharField(max_length=255)

    last_updated = models.DateTimeField(auto_now_add=True)

    carta = models.ForeignKey(Carta, related_name='topics', on_delete = models.CASCADE)

    starter = models.ForeignKey(User, on_delete = models.CASCADE, related_name='topics')

class Post(models.Model):

    message = models.TextField(max_length=4000)

    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')
