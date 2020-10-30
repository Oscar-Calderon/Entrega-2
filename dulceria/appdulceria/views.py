from django.shortcuts import render,redirect
from appdulceria.forms import UsuarioForm
from appdulceria.models import Usuario
# Create your views here.

def usuario(request):
    if request.method == "POST": 
        usuario_f = Usuario(rut = request.POST['rut'],
                            nombre = request.POST['nombre'],
                            apellido_paterno = request.POST['apellidoP'],
                            apellido_materno = request.POST['apellidoM'],
                            nick = request.POST['nick'],
                            correo = request.POST['correo'],
                            fecha_nacimiento = request.POST['fecha'],
                            contrasena = request.POST['contrasena']
                            )
        usuario_f.save()
    return render(request,'registro.html')