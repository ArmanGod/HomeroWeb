from django import template
from django.shortcuts import render, redirect
from .models import Incidente, Servidor, Sistema, NivelSensibilidad, Usuario
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import   datetime
import base64


# Create your views here.



def  index(request):
    if request.method=='POST':
        inicio = Usuario.objects.get(rut=request.POST['usuario'])
        a = inicio.contrasena
        f = base64.b64decode(a).decode('utf-8')
        if f == request.POST['contrasena']:
            if inicio.cargo == 'informante' or inicio.cargo == 'responsable':
                request.session['rut']=inicio.rut
                return render(request, 'Homero/menu.html')
            else:
                return render(request, 'Homero/menu.html')
    return render(request, 'Homero/index.html')

def menu(request):
    return render(request, 'Homero/menu.html')
def correo(request):
    return render(request, 'Homero/correo.html')
def send_email(mail,sist, nombre):
    sistema = Sistema.objects.get(id_sistema=sist)
    nivelSens = NivelSensibilidad.objects.all()
    context = {'sist':sist, 'sistema':sistema,'nivelSens':nivelSens, 'nombre':nombre}
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
        sistema = Sistema()
        sistema.id_sistema = request.POST.get('cboSistema')
        incidente.id_sistema = sistema
        incidente.problema = request.POST.get('problema')
        incidente.solucion = request.POST.get('solucion')
        fecha = datetime.date.today()
        incidente.fecha_inci = fecha
        if incidente.id_sistema == sistema:
            sistema2 = Sistema.objects.get(id_sistema=incidente.id_sistema)
            usuario = Usuario.objects.get(rut=sistema2.rut)
            nombre = usuario.primer_nombre + ' ' + usuario.apellido_paterno
            incidente.responsable_solucion = nombre
            mail = usuario.correo_electronico 
        sist = request.POST.get('cboSistema')
        incidente.save()
        send_email(mail,sist,nombre)



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
    