from django import forms
from django.contrib.auth.models import User
from .models import Element, Bland, UserProfile, Prestamo, DetallePrestamo


class AddElementForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = ('bland', 'element_type', 'serial', 'serial_sena', 'modelo', 'features')


class AddBlandForm(forms.ModelForm):

    class Meta:
        model = Bland
        fields = ('bland_name',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('nombre', 'apellido', 'email', 'documento', 'document_type', 'role')


class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = ('fecha', 'hora_inicio', 'hora_fin')


class PrestaForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = ('fecha', 'hora_inicio', 'hora_fin', 'devolucion')


class DetalleForm(forms.ModelForm):

    class Meta:
        model = DetallePrestamo
        fields = ('element', )
