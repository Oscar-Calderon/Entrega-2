import django_filters
from django_filters import DateFilter, CharFilter

from appdulceria.models import Usuario

class UsuarioFiltro(django_filters.FilterSet):
    fecha_n_inicio = DateFilter(field_name="fecha_nacimiento", lookup_expr='gte')
    fecha_n_termino = DateFilter(field_name="fecha_nacimiento", lookup_expr='lte')

    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['fecha_nacimiento']