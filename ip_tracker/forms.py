from django import forms
from .models import Network
from django.forms.widgets import DateInput

class NetworkForm(forms.ModelForm):
	class Meta:
		model = Network
		fields = ['office', 'device', 'ip_address', 'gateway', 'serial_number', 'configured', 'date', 'remarks', 'images']
		widgets = {
            'date': DateInput(attrs={'type': 'date'}),
			'remarks': forms.TextInput(attrs={'placeholder': 'Enter your comments'}),
        }