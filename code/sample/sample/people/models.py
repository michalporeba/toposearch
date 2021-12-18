import uuid
from django.db import models

# Create your models here.

class MyBaseModel(models.Model):
    uniqueId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta: 
        abstract = True 


class Person(MyBaseModel):
    serviceInstance = models.PositiveIntegerField("Service instance", blank=True, null=True)
    firstName = models.CharField("First name", max_length=128, blank=False, null=False)
    lastName = models.CharField("Last name", max_length=128, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=8, blank=True, null=True)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"