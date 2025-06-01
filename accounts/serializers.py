from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#prueba de usuario que se añada
from rest_framework import serializers
from api.models import Usuario
from django.contrib.auth.hashers import make_password

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['rol'] = self.user.rol  # Solo si tu modelo Usuario tiene campo 'rol'
        data['nombre'] = f"{self.user.first_name} {self.user.last_name}"
        data['email'] = self.user.email
        return data



class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['rol'] = 'Cliente'  # Asigna el rol por defecto
        return Usuario.objects.create(**validated_data)
    
#usuario se registra
class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['rol'] = 'Cliente'  # o 'Usuario' según tu estructura
        return Usuario.objects.create(**validated_data)