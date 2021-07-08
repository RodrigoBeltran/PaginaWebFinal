from django.contrib import admin
from .models import Marca, Rams, Juegos, Gabinete,Procesador, GPU
# Register your models here.

admin.site.register(Marca)
admin.site.register(Rams)
admin.site.register(Juegos)
admin.site.register(Gabinete)
admin.site.register(Procesador)
admin.site.register(GPU)
