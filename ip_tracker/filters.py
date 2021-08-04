import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput
from .models import Network

class NetworkFilter(django_filters.FilterSet):
    office = CharFilter(field_name='office', lookup_expr='icontains')
    device = CharFilter(field_name='device', lookup_expr='icontains')
    serial_number = CharFilter(field_name='serial_number', lookup_expr='icontains')
    class Meta:
        model = Network
        fields = ['office','device', 'serial_number']    