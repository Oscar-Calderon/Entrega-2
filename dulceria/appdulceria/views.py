from django.shortcuts import render, redirect
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
        return redirect('/login')
    return render(request,'registro.html')

def modificar(request,rut):
    usu = Usuario.objects.get(rut=rut)
    form = UsuarioForm(instance=usu)
    return render(request,'modificar.html',{'form':form,'rut':usu.rut})

def clientes(request):
    form = UsuarioForm()
    l_clientes = Usuario.objects.all()
    return render(request,'gestion_usuarios.html',{'form':form,'clientes':l_clientes})
        


#def modificar_confirmar(request,rut):
 #   usu = Usuario.objects.get(rut=rut)
  #  if request