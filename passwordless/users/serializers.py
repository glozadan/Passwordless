from users.models import User

#Imports for the validators
from rest_framework.serializers import ValidationError
from rest_framework import serializers

#Imports for password encryption
from django.contrib.auth.hashers import make_password


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'is_active',
            'is_verified',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'password':{'write_only': True},
        }

        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }

    def validate(self, data):
        username = data.get('username')
        #email = data.get('email')
        password = data.get('password')
        errors = dict()
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]-./=?¿<>"


        if len(username) < 6: 
            raise ValidationError({"error": "El nombre de usuario debe tener un mínimo de 6 caracteres"})

        if len(username) > 20: 
            raise ValidationError({"error": "El nombre de usuario debe tener un máximo de 20 caracteres"})


        if any(i in special_characters for i in username): 
           raise ValidationError({"error": "El nombre de usuario no admite caracteres especiales"})

        if any(i.isspace() for i in username): 
            raise ValidationError({"error": "El nombre de usuario no admite espacios en blanco"})

        if not any(i.isalpha() for i in password):
            raise ValidationError({"error": "La contraseña debe incluir al menos una letra"})
        
        if not any(i.isupper() for i in password):
            raise ValidationError({"error": "La contraseña debe incluir al menos una letra mayúscula"})
        
        if not any(i.isdigit() for i in password):
            raise ValidationError({"error": "La contraseña debe incluir al menos un dígito"})
        
        if not any(i in special_characters for i in password): 
            raise ValidationError({"error": "La contraseña debe incluir al menos un caracter especial"})

        if any(i.isspace() for i in password):
            raise ValidationError({"error": "La contraseña no debe incluir espacios en blanco"})

        if any(i.isspace() for i in password): 
            raise ValidationError({"error": "La contraseña no debe incluir espacios"})
        
        if any(i.isspace() for i in password):
            raise ValidationError({"error": "La contraseña no admite espacios en blanco"})
        
        if len(password) > 20:
            raise ValidationError({"error":"La contraseña debe tener un máximo 20 caracteres"})
        
        if len(password) < 6:
            raise ValidationError({"error": "La contraseña debe tener un mínimo de 6 caracteres"})
        
        if errors:
            raise ValidationError(errors)
        
        return super(UserSignUpSerializer, self).validate(data)

        
        
        
    #Token encryption.
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSignUpSerializer, self).create(validated_data)

#Login 
class UserLoginSerializer(serializers.ModelSerializer):
    # Campos que vamos a requerir
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=20)
    class Meta: 
        model = User
        fields = [
            'email', 
            'password',
            'is_active',
            'is_verified',
        ]

