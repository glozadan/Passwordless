from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin



# Create your models here.

# Custom manager.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username: 
           raise TypeError("Ingresa un nombre de usuario válido")
      
        if not email:
            raise TypeError("Enter a valid email address.")
        if not password:
            raise TypeError("Enter a valid password.")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_active=True
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise TypeError("Introduce un correo electrónico válido.")
        if not password:
            raise TypeError("Introduce una contraseña válida.")

        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )
        user.email = email
        user.set_password(password)
        user.save()
        return user

# Custom User model.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True, default=False) 
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username