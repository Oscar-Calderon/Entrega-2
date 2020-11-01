"""dulceria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import appdulceria.views
from dulceria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='inicio'),
    path('registro/',views.registro,name='registro'),
    path('login/',views.login,name='login'),
    path('productos/',views.productos,name='productos'),
    path('recuperar/',views.recuperar,name='recuperar'),
    path('usuario/',appdulceria.views.usuario,name='usuario'),
    path('gestion_usuarios/',views.gestion_usuarios,name='gestion_usuarios'),
    path('editar/<rut>/',appdulceria.views.editar),
    path('modificar/<rut>/',appdulceria.views.modificar),
    path('clientes/',appdulceria.views.clientes),
    path('eliminar/<rut>/',appdulceria.views.eliminar)
]
