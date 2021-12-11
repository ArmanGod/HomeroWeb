from django import template
from django.shortcuts import render, redirect
from .models import Incidente, Servidor, Sistema, Usuario
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import   datetime

# Create your views here.

def  index(request):
    return render(request, 'Homero/index.html')

def menu(request):
    return render(request, 'Homero/menu.html')
def correo(request):
    return render(request, 'Homero/correo.html')
def send_email(mail,sist):
    sistema = Sistema.objects.get(id_sistema=sist)
    context = {'sist':sist, 'sistema':sistema}
    template = get_template('Homero/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Titulo',
        'Asunto',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

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
        mail = request.POST.get('mantenedor')
        sist = request.POST.get('cboSistema')
        try:
            incidente.save()
            send_email(mail,sist)
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
def modificar(request, id):
    modificar = Incidente.objects.get(id_incidente=id)
    sistemas = Sistema.objects.all()
    data4 = {
        'modificar':modificar,
        'sistemas':sistemas
    }
    if request.POST:
        incidente = Incidente()
        incidente.id_incidente = request.POST.get('txtId')
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
            data4['mensaje'] = 'No se ha podido Modificar'
        return redirect('adminIncidente')
    return render(request,'Homero/modificar.html',data4)
    