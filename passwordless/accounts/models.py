from django.db import models
from django_cryptography.fields import encrypt
from users.models import User

# Create your models here.

class Account(models.Model):

    types = [
        ('Banca', 'Banca'),
        ('Red social', 'Red social'),
        ('Correo electrónico', 'Correo electrónico'),
        ('Otro', 'Otro')
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = False)
    account_name = models.CharField(max_length = 30)
    account_type = models.CharField(max_length = 20, choices = types)
    account_description = models.CharField(max_length = 50, blank = True)
    account_username = models.CharField(max_length = 35)
    account_password = encrypt(models.CharField(max_length = 35))

    class Meta:
        db_table = 'accounts'
    
    def __str__(self):
        return self.account_name
