from django.shortcuts import render,redirect
from appdulceria.forms import UsuarioForm
from appdulceria.models import Usuario
# Create your views here.

def usuario(request):
    if request.method == "POST":
        registro = UsuarioForm(request.POST)
        if registro.is_valid():
            try:
                registro.save()
                return redirect('/usuario')
            except:
                pass
    else:
        registro = UsuarioForm()
        usuario = Usuario.objects.all()
    return render(request,'registro.html',{'registro': registro, 'usuario': usuario})