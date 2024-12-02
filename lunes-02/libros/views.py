from django.shortcuts import render,redirect
from .models import Libro

# Create your views here.
def generar_libro(request):
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        genero=request.POST.get('genero')
        fecha_publicacion=request.POST.get('fecha_publicacion')
        Libro.objects.create(nombre=nombre,descripcion=descripcion,genero=genero,fecha_publicacion=fecha_publicacion)
        return redirect('listar_libros.html')
    return render

def listar_libros(request):
    libros=Libro.objects.all()
    return render (request,'listar_libros.html',{'libros':libros})