from django import template
from django.shortcuts import render, redirect

from HomeroWeb.settings import DATABASES
from .models import Incidente, SalaServidor, Servidor, Sistema, NivelSensibilidad, Usuario, SysSerDet, Rack, SalaServidor
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import datetime
import base64
from django.db.models import Count



# Create your views here.

def  index(request):
    try:
        if request.method=='POST':
            inicio = Usuario.objects.get(rut=request.POST['usuario'])
            a = inicio.contrasena
            f = base64.b64decode(a).decode('utf-8')
            if f == request.POST['contrasena']:
                if inicio.cargo == 'Informante' or inicio.cargo == 'Responsable':
                    request.session['rut']=inicio.rut
                    return render(request, 'Homero/menu.html')
                if inicio.cargo == 'Consultor':
                    request.session['rut']=inicio.rut
                    return render(request, 'Homero/menuCon.html')
                if inicio.cargo == 'Mantenedor':
                    request.session['rut']=inicio.rut
                    return render(request, 'Homero/menuMan.html')
                if inicio.cargo == 'Administrador':
                    request.session['rut']=inicio.rut
                    return render(request, 'Homero/menuAdmin.html')
    except:
            return render(request, 'Homero/index.html')     
    return render(request, 'Homero/index.html')
def menuAdmin(request):
    return render(request, 'Homero/menuAdmin.html')
def menuMan(request):
    return render(request, 'Homero/menuMan.html')
def menu(request):
    return render(request, 'Homero/menu.html')
def menuCon(request):
    return render(request, 'Homero/menuCon.html')
def correo(request):
    return render(request, 'Homero/correo.html')
def correo2(request):
    return render(request, 'Homero/correo2.html')
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

def send_email2(mail,servs,nombre):
    servidor = Servidor.objects.get(id_servidor = servs)
    context = {'servs':servs,'servidor':servidor,'nombre':nombre}
    template = get_template('Homero/correo2.html')
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
        incidente.tiempo_inactividad = 0
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
        try:
            incidente.save()
            send_email(mail,sist,nombre)
        except:
            return render(request, 'Homero/adminIncidentes.html')
    return render(request, 'Homero/incidentes.html', data2)

def incidentesServ(request):
    servidor = Servidor.objects.all()
    data = {
        'servidor': servidor
    }
    if request.POST:
        incidente = Incidente()
        incidente.id_incidente = "asd"
        incidente.tipo_incidente = request.POST.get('tipo')
        incidente.nombre_incidente = request.POST.get('nombre')
        incidente.tiempo_inactividad = 0
        servidor = Servidor()
        servidor.id_servidor = request.POST.get('cboServidor')
        incidente.id_servidor = request.POST.get('cboServidor')
        fecha = datetime.date.today()
        incidente.fecha_inci = fecha
        incidente.problema = request.POST.get('problema')
        incidente.solucion =request.POST.get('solucion')
        servidor2 = Servidor.objects.get(id_servidor = incidente.id_servidor)
        usuario = Usuario.objects.get(rut=servidor2.rut)
        nombre = usuario.primer_nombre + ' ' + usuario.apellido_paterno
        incidente.responsable_solucion = nombre
        mail = usuario.correo_electronico
        servs = request.POST.get('cboServidor')
        try:
            incidente.save()
            send_email2(mail,servs,nombre)
        except:
            return render(request, 'Homero/adminIncidentes.html')
    return render(request,'Homero/incidentesServ.html',data)

def consultaSisCon(request):
    sistema = Sistema.objects.all()
    servidor = Servidor.objects.all()
    sys = SysSerDet.objects.all()
    data = {
        'sistema':sistema,
        'servidor':servidor,
        'sys':sys
    }
    return render(request,'Homero/consultaSisCon.html',data)

def consultaSistema(request):
    sistema = Sistema.objects.all()
    servidor = Servidor.objects.all()
    sys = SysSerDet.objects.all()
    data = {
        'sistema':sistema,
        'servidor':servidor,
        'sys':sys
    }
    return render(request,'Homero/consultaSistema.html',data)

def consultaServCon(request):
    servidores = Servidor.objects.all()
    rack = Rack.objects.all()
    sala = SalaServidor.objects.all()
    data = {
        'servidores': servidores,
        'rack':rack,
        'sala':sala
    }
    return render(request, 'Homero/consultaServCon.html', data)
def consultarServMan(request):
    servidores = Servidor.objects.all()
    rack = Rack.objects.all()
    sala = SalaServidor.objects.all()
    data = {
        'servidores': servidores,
        'rack':rack,
        'sala':sala
    }
    return render(request, 'Homero/consultarServMan.html', data)
def consultaServ(request):
    servidores = Servidor.objects.all()
    rack = Rack.objects.all()
    sala = SalaServidor.objects.all()
    data = {
        'servidores': servidores,
        'rack':rack,
        'sala':sala
    }
    return render(request, 'Homero/consultaServidor.html', data)

def adminIncidente(request):
    incidentes = Incidente.objects.all()
    data3 = {
        'incidentes':incidentes
    }
    return render(request, 'Homero/adminIncidente.html',data3)

def modificarServ(request, id):
    modificar = Incidente.objects.get(id_incidente=id)
    servidores = Servidor.objects.all()
    data = {
        'modificar':modificar,
        'servidores':servidores
    }
    if request.POST:
        incidente = Incidente()
        incidente.id_incidente = request.POST.get('txtId')
        incidente.tipo_incidente = request.POST.get('tipo')
        incidente.nombre_incidente = request.POST.get('nombre')
        incidente.tiempo_inactividad = request.POST.get('tiempo')
        servidor = Servidor()
        servidor.id_servidor = request.POST.get('cboServidor')
        incidente.id_servidor = request.POST.get('cboServidor')
        fecha = datetime.date.today()
        incidente.fecha_inci = fecha
        incidente.problema = request.POST.get('problema')
        incidente.solucion =request.POST.get('solucion')
        servidor2 = Servidor.objects.get(id_servidor = incidente.id_servidor)
        usuario = Usuario.objects.get(rut=servidor2.rut)
        nombre = usuario.primer_nombre + ' ' + usuario.apellido_paterno
        incidente.responsable_solucion = nombre
        try:
            incidente.save()
            return redirect('adminIncidente')
        except:
            return render(request, 'Homero/adminIncidentes.html')
    return render(request, 'Homero/modificarServ.html', data)

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
        try:
            incidente.save()
            return redirect('adminIncidente')
        except:
            return render(request, 'Homero/adminIncidentes.html')
    return render(request,'Homero/modificar.html',data4)

def dashboard(request,**kwargs):
    from datetime import datetime
    data2 = []
    fecha = datetime.now().year
    for m in range(1, 13):
        total = Incidente.objects.filter(fecha_inci__year = fecha, fecha_inci__month=m).aggregate(r=Count('id_incidente')).get('r')
        data2.append(total)
    data = {
        'data2':data2
    }
    return render(request, 'Homero/dashboard.html',data)

def dashboard2(request,**kwargs):
    data2 = []
    principal = SysSerDet.objects.filter(tipo_relacion = "Principal").aggregate(r=Count('tipo_relacion')).get('r')
    secundario = SysSerDet.objects.filter(tipo_relacion = "Secundario").aggregate(r=Count('tipo_relacion')).get('r')
    contingencia = SysSerDet.objects.filter(tipo_relacion = "Contingencia").aggregate(r=Count('tipo_relacion')).get('r')
    if principal >= 1:
        data2.append(principal)
    if secundario >= 1:
        data2.append(secundario)
    if contingencia >= 1:
        data2.append(contingencia)
    else:
        data2.append(0)
    data = {
        'data2':data2
    }
    return render(request, 'Homero/dashboard2.html',data)
