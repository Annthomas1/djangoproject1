from django.db import models

# Create your models here.
class credentials(models.Model):
    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    confirmpassword = models.CharField(max_length=250)
