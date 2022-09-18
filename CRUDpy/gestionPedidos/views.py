#  from curses.ascii import HTTP 
from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
from django.template import loader
from gestionPedidos.models import Articulos
from gestionPedidos.forms import FormularioContacto

import datetime

def saludo(request):
    nombre = "Maria"
    apellido = "Gonzales"
    temas = ["Plantillas","Modelos", "formularios","Vistas"]
    fecha = datetime.datetime.now()
    return render(request, "plantilla.html", {"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha,"temas_curso":temas})

def curso(request):
    fecha = datetime.datetime.now()
    return render(request,"curso.html",{"now":fecha})

def saludo_html(request):
    documento="""<html><body><h1>Hola a todos!</h1></body></html>"""
    return HttpResponse(request, documento)

def despedida(request):
    return HttpResponse(request, "Hasta luego!")

def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>Fecha: %s</h1></body></html>"""%fecha_actual
    return HttpResponse(request, documento)

def pedidos(request):
    fecha = datetime.datetime.now()
    return render(request,"pedidos.html",{"now":fecha})

def busqueda_productos(request):
    return render(request,"busqueda_productos.html")

def buscar(request):
    if request.GET["prd"]:
        producto=request.GET["prd"]
        if len(producto)>20:
            mensaje="Texto de búsqueda demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
        return render(request,"resultados_busqueda.html",{"articulos":articulos,"query":producto})
    else:
        mensaje="No has introducido ningún dato"
        return HttpResponse(request, mensaje)


def contacto(request):
    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            return render(request,"gracias.html")
    else:
        miFormulario=FormularioContacto()
        return render(request,"formulario_contacto.html",{"form":miFormulario})
