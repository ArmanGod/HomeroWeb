# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaBd(models.Model):
    id_aud_bd = models.CharField(primary_key=True, max_length=20)
    id_bd = models.CharField(max_length=20)
    nombre_bd = models.CharField(max_length=20)
    motor_bd = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=200)
    id_servidor = models.CharField(max_length=20)
    id_tipo = models.FloatField()
    id_sistema = models.CharField(max_length=20)
    fech_aud_bd = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_bd'


class AuditoriaRack(models.Model):
    id_aud_rack = models.CharField(primary_key=True, max_length=20)
    id_rack = models.CharField(max_length=20)
    espacio_disponible = models.FloatField()
    espacio_ocupado = models.FloatField()
    espacio_total = models.FloatField()
    tipo_rack = models.CharField(max_length=20)
    disponibilidad = models.CharField(max_length=1)
    id_sala = models.CharField(max_length=20)
    fech_aud_rack = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_rack'


class AuditoriaSala(models.Model):
    id_aud_sala = models.CharField(primary_key=True, max_length=20)
    id_sala = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    metros_cuadrados = models.FloatField()
    descripcion = models.CharField(max_length=200)
    extintor = models.CharField(max_length=1)
    refrigeracion_sala = models.CharField(max_length=1)
    reconocimiento_huellas = models.CharField(max_length=1)
    monitoreo = models.CharField(max_length=1)
    pasa_cables = models.CharField(max_length=1)
    fech_aud_sala = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_sala'


class AuditoriaServicio(models.Model):
    id_aud_servicio = models.CharField(primary_key=True, max_length=20)
    id_servicio = models.FloatField()
    nombre_servicio = models.CharField(max_length=20)
    id_tipo = models.FloatField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fech_aud_servicio = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_servicio'


class AuditoriaServidor(models.Model):
    id_aud_serv = models.CharField(primary_key=True, max_length=20)
    id_servidor = models.CharField(max_length=20)
    nombre_servidor = models.CharField(max_length=20)
    sistema_operativo = models.CharField(max_length=20)
    capacidad_disco = models.FloatField()
    ram = models.FloatField()
    garantia = models.CharField(max_length=1)
    contrasena_admin = models.CharField(max_length=200)
    direccion_ip = models.CharField(max_length=20)
    rut_mantenedor = models.CharField(max_length=12)
    id_rack = models.CharField(max_length=20)
    rut = models.CharField(max_length=12)
    id_tipo = models.FloatField()
    fech_aud_serv = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_servidor'


class AuditoriaSistema(models.Model):
    id_aud_sistema = models.CharField(primary_key=True, max_length=20)
    id_sistema = models.CharField(max_length=20)
    nombre_sistema = models.CharField(max_length=20)
    lenguaje_sistema = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=20)
    id_sensibilidad = models.CharField(max_length=20)
    rut = models.CharField(max_length=12)
    id_nivel = models.FloatField()
    fech_aud_sistema = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_sistema'


class AuditoriaUsuario(models.Model):
    id_aud_user = models.CharField(primary_key=True, max_length=20)
    rut = models.CharField(max_length=12)
    primer_nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono_empresa = models.FloatField()
    telefono_personal = models.FloatField()
    cargo = models.CharField(max_length=20)
    correo_electronico = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)
    id_perfil = models.FloatField()
    fech_aud_user = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bd(models.Model):
    id_bd = models.CharField(primary_key=True, max_length=20)
    nombre_bd = models.CharField(max_length=20)
    motor_bd = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=200)
    id_servidor = models.ForeignKey('Servidor', models.DO_NOTHING, db_column='id_servidor', blank=True, null=True)
    id_sistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='id_sistema')
    id_tipo = models.ForeignKey('TipoBd', models.DO_NOTHING, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'bd'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documento(models.Model):
    id_documento = models.CharField(primary_key=True, max_length=20)
    nom_doc = models.CharField(max_length=20)
    archivo = models.BinaryField()
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)
    id_sistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='id_sistema', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento'


class Incidente(models.Model):
    id_incidente = models.CharField(primary_key=True, max_length=20)
    tipo_incidente = models.CharField(max_length=20)
    nombre_incidente = models.CharField(max_length=20)
    problema = models.CharField(max_length=200)
    solucion = models.CharField(max_length=200)
    tiempo_inactividad = models.FloatField()
    responsable_solucion = models.CharField(max_length=20)
    id_sistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='id_sistema')
    fecha_inci = models.DateField()
    def __str__(self):
        return self.id_incidente
    class Meta:
        managed = False
        db_table = 'incidente'


class NivelSeguridad(models.Model):
    id_nivel = models.FloatField(primary_key=True)
    nivel = models.FloatField()
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'nivel_seguridad'


class NivelSensibilidad(models.Model):
    id_sensibilidad = models.CharField(primary_key=True, max_length=20)
    nombre_sensibilidad = models.CharField(max_length=20)
    nivel = models.FloatField()

    class Meta:
        managed = False
        db_table = 'nivel_sensibilidad'


class PerfilUsuario(models.Model):
    id_perfil = models.FloatField(primary_key=True)
    tipo_perfil = models.CharField(max_length=20)
    nivel_perfil = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'perfil_usuario'


class Rack(models.Model):
    id_rack = models.CharField(primary_key=True, max_length=20)
    espacio_disponible = models.FloatField()
    espacio_ocupado = models.FloatField()
    espacio_total = models.FloatField()
    tipo_rack = models.CharField(max_length=20)
    disponibilidad = models.CharField(max_length=1)
    id_sala = models.ForeignKey('SalaServidor', models.DO_NOTHING, db_column='id_sala')

    class Meta:
        managed = False
        db_table = 'rack'


class SalaServidor(models.Model):
    id_sala = models.CharField(primary_key=True, max_length=20)
    direccion = models.CharField(max_length=20)
    metros_cuadrados = models.FloatField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    extintor = models.CharField(max_length=1)
    refrigeracion_sala = models.CharField(max_length=1)
    reconocimiento_huellas = models.CharField(max_length=1)
    monitoreo = models.CharField(max_length=1)
    pasa_cables = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sala_servidor'


class Servicio(models.Model):
    id_servicio = models.CharField(primary_key=True, max_length=20)
    nombre_servicio = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    id_tipo = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'servicio'


class Servidor(models.Model):
    id_servidor = models.CharField(primary_key=True, max_length=20)
    nombre_servidor = models.CharField(max_length=20)
    sistema_operativo = models.CharField(max_length=20)
    capacidad_disco = models.FloatField()
    ram = models.FloatField()
    garan = models.CharField(max_length=1)
    contrasena_admin = models.CharField(max_length=200)
    direccion_ip = models.CharField(max_length=20)
    rut_mantenedor = models.CharField(max_length=12)
    id_rack = models.ForeignKey(Rack, models.DO_NOTHING, db_column='id_rack')
    rut = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='rut')
    id_tipo = models.ForeignKey('TipoServidor', models.DO_NOTHING, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'servidor'


class Sistema(models.Model):
    id_sistema = models.CharField(primary_key=True, max_length=20)
    nombre_sistema = models.CharField(max_length=20)
    lenguaje_sistema = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=20)
    id_sensibilidad = models.ForeignKey(NivelSensibilidad, models.DO_NOTHING, db_column='id_sensibilidad')
    rut = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='rut')
    id_nivel = models.ForeignKey(NivelSeguridad, models.DO_NOTHING, db_column='id_nivel')
    ordenar = models.FloatField()
    def __str__(self):
        return self.id_sistema

    class Meta:
        managed = False
        db_table = 'sistema'


class SysSerDet(models.Model):
    id_servidor = models.OneToOneField(Servidor, models.DO_NOTHING, db_column='id_servidor', primary_key=True)
    id_sistema = models.ForeignKey(Sistema, models.DO_NOTHING, db_column='id_sistema')
    tipo_relacion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_ser_det'
        unique_together = (('id_servidor', 'id_sistema'),)


class SysServDet(models.Model):
    id_servicio = models.OneToOneField(Servicio, models.DO_NOTHING, db_column='id_servicio', primary_key=True)
    id_sistema = models.ForeignKey(Sistema, models.DO_NOTHING, db_column='id_sistema')
    tipo_relacion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_serv_det'
        unique_together = (('id_servicio', 'id_sistema'),)


class TipoBd(models.Model):
    id_tipo = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_bd'


class TipoServicio(models.Model):
    id_tipo = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_servicio'


class TipoServidor(models.Model):
    id_tipo = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_servidor'


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    primer_nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono_empresa = models.FloatField()
    telefono_personal = models.FloatField()
    correo_electronico = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)
    cargo = models.CharField(max_length=20)
    id_perfil = models.ForeignKey(PerfilUsuario, models.DO_NOTHING, db_column='id_perfil')

    class Meta:
        managed = False
        db_table = 'usuario'