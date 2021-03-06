import datetime
from django.db import models
from django.contrib.auth.models import User


class Bland(models.Model):
    bland_name = models.CharField(max_length=60)

    def __str__(self):
        return self.bland_name


class Role(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name


class ElementType(models.Model):
    element_type = models.CharField(max_length=100)

    def __str__(self):
        return self.element_type


class Element(models.Model):
    bland = models.ForeignKey(Bland)
    element_type = models.ForeignKey(ElementType)
    opciones = ((1, 'Disponible'), (2, 'Ocupado'), (3, 'Mantenimiento'))
    state = models.IntegerField(choices=opciones, default=1)
    serial_sena = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    features = models.TextField(blank=True)

    def __str__(self):
        return self.modelo


class UserProfile(models.Model):
    username = models.OneToOneField(User, unique=True)
    nombre = models.CharField(blank=True, max_length=100)
    apellido = models.CharField(blank=True, max_length=100)
    email = models.EmailField()
    opciones = ((1, 'CC'), (2, 'Pasaporte'), (3, 'TI'))
    document_type = models.IntegerField(choices=opciones, default=1)
    documento = models.IntegerField(unique=True)
    role = models.ForeignKey(Role)

    def __str__(self):
        return self.username.username


class Prestamo(models.Model):
    user = models.ForeignKey(UserProfile)
    fecha = models.DateField(default=datetime.datetime.today)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    devolucion = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey(Prestamo)
    element = models.ForeignKey(Element)

    def __str__(self):
        return str(self.prestamo)
