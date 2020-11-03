from django.test import TestCase

# Create your tests here.
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from appdulceria.models import Usuario, Producto
from dulceria.views import index, registro
from appdulceria.forms import EditarForm

# Esta prueba es para probar las URL y si esta tomando efectivamente las views correspondientes
class TestUrls(SimpleTestCase):

    def test_inicio_url(self):
        url=reverse('inicio')
        self.assertEqual(resolve(url).func, index)

    def test_registro_url(self):
        url=reverse('registro')
        self.assertEqual(resolve(url).func, registro)

#Pruebas de formulario
class TestForms(SimpleTestCase):

    #No se puede editar un formulario de usuario si no se ingresan datos
    def test_editar_formulario_vacio(self):
        form = EditarForm(data={})
        self.assertFalse(form.is_valid())


#Pruebas de modelos
class TestModels(TestCase):

    def test_creacion_producto(self):
        productoNuevo = Producto.objects.create(id_producto="JJ01", nombre="Bombones de carne", valor="1000")
        self.assertTrue(productoNuevo.nombre, "Bombones de carne")
