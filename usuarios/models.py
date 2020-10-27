from django.db import models

class TipoUsuario(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50,null=False)
class Usuario(models.Model):
    rut = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=100,null=False)
    apellidoPaterno = models.CharField(max_length=100,null=False)
    apellidoMaterno = models.CharField(max_length=100,null=False)
    nick = models.CharField(max_length=15,null=False)
    correo = models.CharField(max_length=60,null=False)
    fechaNacimiento = models.DateField(null=False)
    contrasena = models.CharField(max_length=50,null=False)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)