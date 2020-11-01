from django import forms
from appdulceria.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class EditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'nick', 'correo', 'fecha_nacimiento', 'contrasena', 'tipoUsuario']

class ContrasenaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['contrasena']

class RutForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut']