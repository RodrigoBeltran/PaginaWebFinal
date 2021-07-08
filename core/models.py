from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Rams(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    capacidad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    formato = models.CharField(max_length=50)
    voltateje = models.CharField(max_length=50)
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="rams", null=True)
     
    def __str__(self):
        return self.nombre

class Juegos(models.Model):
    nombre = models.CharField(max_length=50)
    procesador = models.CharField(max_length=60)
    memoria = models.CharField(max_length=60)
    graficos = models.CharField(max_length=80)
    almacenamiento = models.CharField(max_length=50)
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    caratula = models.ImageField(upload_to="games", null=True)

    def __str__(self):
        return self.nombre

class Gabinete(models.Model):
    nombre = models.CharField(max_length=50)
    formato = models.CharField(max_length=50)
    fuentePoder = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    panel = models.CharField(max_length=50)
    ventiladores = models.CharField(max_length=50)
    precio = models.IntegerField()
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="gabinetes", null=True)

    def __str__(self):
        return self.nombre        

class Procesador(models.Model):
    nombre = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    nucleos = models.CharField(max_length=50)
    socket = models.CharField(max_length=50)
    cache = models.CharField(max_length=50)
    arquitectura = models.CharField(max_length=50)
    precio = models.IntegerField()
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="procesadores", null=True)

    def __str__(self):
        return self.nombre


class GPU(models.Model):
    nombre = models.CharField(max_length=50)
    memoria = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    nucleos = models.CharField(max_length=50)
    precio = models.IntegerField()
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="Graficos", null=True)

    def __str__(self):
        return self.nombre