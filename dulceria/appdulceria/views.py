from django.shortcuts import render, redirect
from appdulceria.forms import UsuarioForm, EditarForm, ContrasenaForm, RutForm
from appdulceria.models import Usuario 
from appdulceria.filters import UsuarioFiltro

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

def modificar(request,rut):
    cli = Usuario.objects.get(rut=rut)
    if request.method == "POST":
        form = EditarForm(request.POST, instance=cli)
        if form.is_valid():
            try:
                form.save()
                redirect('/clientes')
            except:
                pass
    l_clientes = Usuario.objects.all()
    form = UsuarioForm()
    cli_filtro = UsuarioFiltro(request.GET, queryset=l_clientes)
    l_clientes = cli_filtro.qs
    return render(request,'gestion_usuarios.html',{'form':form, 'clientes':l_clientes,'cli_filtro':cli_filtro})

def eliminar(request, rut):
    cli = Usuario.objects.get(rut=rut)
    cli.delete()
    l_clientes = Usuario.objects.all()
    form = UsuarioForm()
    return render(request,'gestion_usuarios.html',{'form':form,'clientes':l_clientes})

def editar_pass(request):
    cli_pass = Usuario(rut = request.POST['rut'])
    cli = Usuario.objects.get(rut=cli_pass.rut)
    form = ContrasenaForm(instance=cli)
    return render(request,'cambiar_pass.html',{'form':form,'cli':cli})

def modificar_pass(request,rut):
    cli = Usuario.objects.get(rut=rut)
    if request.method == "POST":
        form = ContrasenaForm(request.POST, instance=cli)
        if form.is_valid():
            try:
                form.save()
                redirect('/login')
            except:
                pass
    return render(request,'login.html')

def clientes(request):
    form = UsuarioForm()
    l_clientes = Usuario.objects.all()

    cli_filtro = UsuarioFiltro(request.GET, queryset=l_clientes)
    l_clientes = cli_filtro.qs
    return render(request,'gestion_usuarios.html',{'form':form,'clientes':l_clientes,'cli_filtro':cli_filtro})