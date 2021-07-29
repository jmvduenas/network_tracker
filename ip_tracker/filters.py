import django_filters
from django.forms.widgets import DateInput
from .models import Network

class NetworkFilter(django_filters.FilterSet):
    class Meta:
        model = Network
        fields = ['office','device', 'date']