from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from api.models import Usuario
from api.serializers import UsuarioSerializer
from django.contrib.auth.hashers import make_password
from .serializers import RegistroSerializer

#para la parte del login en JWT
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'username': user.username,
            })
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        return Response(
            {"message": "Logout simulado. El token expirará automáticamente."},
            status=status.HTTP_200_OK
        )
        
#prueba del login 
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#Registro de usuario
class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario registrado exitosamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CrearUsuarioView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Solo permite si es Superadmin
        if not hasattr(request.user, 'rol') or request.user.rol != "Superadmin":
            return Response({"error": "No tienes permisos para crear usuarios."}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data.copy()
        if 'password' in data:
            data['password'] = make_password(data['password'])  # Encripta la contraseña

        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
