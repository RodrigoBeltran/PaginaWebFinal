from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import html
from .models import GPU, Juegos, Rams, Gabinete, Procesador
from .forms import RamsForm, JuegosForm, GabineteForm, ProcesadorForm, GpuForm
from rest_framework import viewsets
from .serializers import RamsSerializer

# Create your views here.


# API REST
class RamsViewset(viewsets.ModelViewSet):
    queryset = Rams.objects.all()
    serializer_class = RamsSerializer


def inicio(request):
    return render(request,"core/inicio.html")

def acerca(request):
    return render(request,"core/acerca.html")

def contacto(request): 
    return render(request,"core/contacto.html")

def juego(request):
    juego = Juegos.objects.all()
    data = {
        'juego': juego
    } 
    return render(request,"core/juego.html", data)

def EnfriamientoCPU(request): 
    return render(request,"core/EnfriamientoCPU.html")

def fuentesDePoder(request): 
    return render(request,"core/fuentesDePoder.html")

def Gabinetes(request):
    gabinete = Gabinete.objects.all()
    data = {
        'gabinete': gabinete
    } 
    return render(request,"core/Gabinetes.html", data)

def PlacaMadre (request):
    return render(request,"core/PlacaMadre.html")

def Procesadores (request):
    proces = Procesador.objects.all()
    data ={
        'proces':proces
    }
    return render(request,"core/Procesadores.html", data)

def SistemasAlmacenamiento (request):
    return render(request,"core/SistemasAlmacenamiento.html")

def TargetasGraficas (request):
    gpu = GPU.objects.all()
    data = {
        'gpu': gpu
    }
    return render(request,"core/TargetasGraficas.html", data)

def TarjetasRam (request):
    rams = Rams.objects.all()
    data = {
        'rams': rams
    }
    return render(request,"core/TarjetasRam.html", data)

def administracion (request):
    return render(request,"core/crud/administracion.html")

# CRUD RAMS
def agregarRams(request):
    data = {
        'form': RamsForm()
    }
    if request.method == 'POST':
        formulario = RamsForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto agregado Correctamente"
        else:
            data["form"] = formulario 
     
    return render(request,"core/crud/rams/add-ram.html", data)     

def modiRams (request, id):
    rams = get_object_or_404(Rams, id=id)

    data ={
        'form': RamsForm(instance=rams)
    }
    if request.method == 'POST':
        formulario = RamsForm(data=request.POST,  instance=rams, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listRam")
        data["form"] = formulario 
    return render(request,"core/crud/rams/modi-ram.html", data) 

def listRam (request):
    rams = Rams.objects.all()

    data ={ 'rams': rams
    }
    return render(request,"core/crud/rams/listRam.html",data)

def eliminar_rams(request, id):
    rams = get_object_or_404(Rams, id=id)
    rams.delete()
    return redirect(to="listRam")


# CRUD Juegos
def agregarJuego(request):
    data = {
        'form': JuegosForm()
    }
    if request.method == 'POST':
        formulario = JuegosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto agregado Correctamente"
        else:
            data["form"] = formulario 
    return render(request,"core/crud/juegos/add-juego.html", data)
def modiJuego (request, id):
    juego = get_object_or_404(Juegos, id=id)

    data ={
        'form': JuegosForm(instance=juego)
    }
    if request.method == 'POST':
        formulario = JuegosForm(data=request.POST,  instance=juego, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listJuego")
        data["form"] = formulario 
    return render(request,"core/crud/juegos/modi-juego.html", data)
def listJuego(request):
    juego = Juegos.objects.all()

    data ={ 'juego': juego
    }
    return render(request,"core/crud/juegos/listJuego.html",data)
def eliminar_Juego(request, id):
    rams = get_object_or_404(Juegos, id=id)
    rams.delete()
    return redirect(to="listJuego")

# CRUD Gabinetes
def agregarGabinete(request):
    data ={
        'form': GabineteForm()
    }
    if request.method=='POST':
        formulario = GabineteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Gabinete agregado Correctamente"
        else:
            data["form"]= formulario    
    return render(request, "core/crud/gabinete/add-gabinete.html", data)

def listGabinete(request):
    gabinete = Gabinete.objects.all()

    data ={ 'gabinete': gabinete
    }
    return render(request,"core/crud/gabinete/listGabinete.html",data)

def modiGabinete(request, id):

    gabinetes = get_object_or_404(Gabinete, id=id)

    data = {
        'form': GabineteForm(instance=gabinetes)
    }
    if request.method == 'POST':
        formulario = GabineteForm(data=request.POST, instance=gabinetes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listGabinete")
        data["form"] = formulario    
    return render(request,"core/crud/gabinete/modi-gabi.html", data)

def eliminar_gabinete(request, id):
    rams = get_object_or_404(Gabinete, id=id)
    rams.delete()
    return redirect(to="listGabinete")

#CRUD Procesadores

def agregarProce(request):
    data={
        'form': ProcesadorForm()
    }

    if request.method == 'POST':
        formulario = ProcesadorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado Correctamente"
        else:
            data["form"]= formulario    
    return render(request, 'core/crud/proces/add-proce.html', data)

def listarProce (request):
    proces = Procesador.objects.all()

    data ={
        'proces': proces
    }
    return render(request,"core/crud/proces/listProce.html", data)

def modificarProce(request, id):
    proces = get_object_or_404(Procesador, id=id)

    data={
        'form': ProcesadorForm(instance=proces)
    }
    if request.method == 'POST':
        formulario = ProcesadorForm(data=request.POST, instance=proces, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarProce")
        data["form"] = formulario    

    return render(request, 'core/crud/proces/modi-proce.html',data)

def eliminar_Proce(request, id):
    proces = get_object_or_404(Procesador, id=id)
    proces.delete()
    return redirect(to="listarProce")

# CRUD  Tarjetas Graficas

def agregarGPU(request):
    data={
        'form': GpuForm()
    }
    if request.method =='POST':
        formulario = GpuForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Guardado Correctamente"
        else:
            data["form"] = formulario   
    return render(request, 'core/crud/Graficos/add-graficos.html', data)

def listarGPU(request):
    gpu = GPU.objects.all()

    data ={
        'gpu': gpu
    }
    return render(request, "core/crud/Graficos/listGraficos.html", data)

def modificarGpu(request, id):
    gpu= get_object_or_404(GPU, id= id)

    data={
        'form': GpuForm(instance=gpu)
    }
    if request.method == 'POST':
        formulario = GpuForm(data=request.POST, instance=gpu, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarGPU")
        data["form"] = formulario 

    return render(request, 'core/crud/Graficos/modi-graficos.html', data)

def eliminar_Gpu(request, id):
    gpu = get_object_or_404(GPU, id=id)
    gpu.delete()
    return redirect(to="listarGPU")
