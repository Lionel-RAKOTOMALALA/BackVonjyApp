from rest_framework import serializers


from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is write-only
        }

    def create(self, validated_data):
        """Create a new user with the provided validated data."""
        return User.objects.create_user(**validated_data)



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Serializer jwt token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token serializer for JWT."""
    
    @classmethod
    def get_token(cls, user):
        """Override the method to add custom claims if needed."""
        token = super().get_token(user)

        # Add custom claims here if needed
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},  # Le mot de passe est facultatif
            'is_active': {'default': True},  # Activer par défaut
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Extraire le mot de passe
        user = User(**validated_data)  # Créer l'utilisateur sans mot de passe pour le moment
        if password:
            user.set_password(password)  # Définir le mot de passe
        user.is_active = True  # Activer l'utilisateur
        user.save()  # Sauvegarder l'utilisateur
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  # On extrait le mot de passe, s'il existe
        activation_token = validated_data.pop('activation_token', None)
        
        # Mettre à jour les autres attributs
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Mettre à jour le mot de passe uniquement s'il a été fourni
        if password:
            instance.set_password(password)
        
        # Gérer le token d'activation si fourni
        if activation_token:
            Token.objects.get_or_create(user=instance, key=activation_token)
        
        instance.save()  # Enregistrer les modifications
        return instance
