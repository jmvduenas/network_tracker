from django import forms
from .models import Network
from django.forms.widgets import DateInput

class NetworkForm(forms.ModelForm):
	class Meta:
		model = Network
		fields = ['office', 'ip_address', 'gateway', 'device', 'configured', 'date', 'remarks']
		widgets = {
            'date': DateInput(attrs={'type': 'date'}),
			'remarks': forms.TextInput(attrs={'placeholder': 'Enter your comments'}),
        }