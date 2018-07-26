from django.db import models

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


