from datetime import date
from django.db import models

# Create your models here.

class Services(models.Model):

            creation_date = models.DateField(default=date.today())
            serial_no = models.CharField(max_length=6, null=True)      
            publication = models.CharField(max_length=6)
            client_name = models.CharField(max_length=100, null=True)
            publish_edition = models.CharField(max_length=100, null=True)
            publish_date = models.DateField(default=date.today)
            particulars = models.CharField(max_length=100, null=True)
            publish_space_position = models.CharField(max_length=100, null=True)
            publish_rate = models.CharField(max_length=100, null=True)
            remarks = models.CharField(max_length=100, null=True)