from django.db import models


class Network(models.Model):
    office = models.CharField(verbose_name="Department", max_length=200)
    ip_address = models.CharField(max_length=200, verbose_name="IP Address")
    gateway = models.CharField(max_length=200, verbose_name="Gateway Address")
    device = models.CharField(max_length=200, verbose_name="Device")
    serial_number = models.CharField(max_length=200, verbose_name="Serial Number", null=True, blank=True)
    configured = models.CharField(max_length=200, verbose_name="Configured by")
    date = models.DateField(verbose_name="Date")
    remarks = models.CharField(max_length=500, verbose_name="Comments")
    images = models.ImageField(null=True, blank=True, upload_to="images/")