from django.contrib import admin
from .models import Network

admin.site.register(Network)

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('office', 'ip_address','device','configured','date')