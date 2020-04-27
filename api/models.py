from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, default='')
    shipment_info = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
