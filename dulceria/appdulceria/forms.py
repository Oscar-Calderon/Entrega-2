from django import forms
from appdulceria.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

'''class EditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '''