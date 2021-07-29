from django.db import models


class Network(models.Model):
    office = models.CharField(verbose_name="Department/Office", max_length=200)
    ip_address = models.CharField(max_length=200, verbose_name="IP Address")
    gateway = models.CharField(max_length=200, verbose_name="Gateway Address")
    device = models.CharField(max_length=200, verbose_name="Device Assigned")
    configured = models.CharField(max_length=200, verbose_name="Configured by")
    date = models.DateField(verbose_name="Date Configured")
    remarks = models.CharField(max_length=500, verbose_name="Comments")
    images = models.ImageField(upload_to='images/')
