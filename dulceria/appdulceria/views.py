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

def editar(request,rut):
    cli = Usuario.objects.get(rut=rut)
    form = UsuarioForm(instance=cli)
    return render(request,'modificar_usuario.html',{'form':form,'rut':cli.rut})

'''def modificar(request,rut):
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
        usuario_f.save()'''

def eliminar(request, rut):
    cli = Usuario.objects.get(rut=rut)
    cli.delete()
    l_clientes = Usuario.objects.all()
    form = UsuarioForm()
    return render(request,'gestion_usuarios.html',{'form':form,'clientes':l_clientes})

def clientes(request):
    form = UsuarioForm()
    l_clientes = Usuario.objects.all()
    return render(request,'gestion_usuarios.html',{'form':form,'clientes':l_clientes})