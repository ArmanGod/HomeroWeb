from django.shortcuts import render
from .models import Incidente, Servidor, Sistema, Usuario
import datetime

# Create your views here.

def  index(request):
    return render(request, 'Homero/index.html')

def menu(request):
    return render(request, 'Homero/menu.html')

def incidentes(request):
    sistema = Sistema.objects.all()
    data2 = {
        'sistema': sistema
    }
    if request.POST:
        incidente = Incidente()
        incidente.id_incidente = "asd"
        incidente.tipo_incidente = request.POST.get('tipo')
        incidente.nombre_incidente = request.POST.get('nombre')
        incidente.tiempo_inactividad = request.POST.get('tiempo')
        incidente.responsable_solucion = request.POST.get('mantenedor')
        sistema = Sistema()
        sistema.id_sistema = request.POST.get('cboSistema')
        incidente.id_sistema = sistema
        incidente.problema = request.POST.get('problema')
        incidente.solucion = request.POST.get('solucion')
        fecha = datetime.date.today()
        incidente.fecha_inci = fecha
        try:
            incidente.save()
        except:
            data2['mensaje'] = 'No se ha podido guardar'



    return render(request, 'Homero/incidentes.html', data2)

def consultaServ(request):
    servidores = Servidor.objects.all()
    data = {
        'servidores': servidores
    }
    return render(request, 'Homero/consultaServidor.html', data)

def adminIncidente(request):
    incidentes = Incidente.objects.all()
    data3 = {
        'incidentes':incidentes
    }
    return render(request, 'Homero/adminIncidente.html',data3)