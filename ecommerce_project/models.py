from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=25, blank=False, null=False)
    # lastname= models.CharField(max_length=25, blank=False, null=False)
    email= models.EmailField(max_length=25, blank=False, null=False)
    password= models.CharField(max_length=128, blank=False, null=False)
    gender= models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name
    