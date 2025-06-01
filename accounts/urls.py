from django.urls import path
from .views import CustomLoginView, LogoutView, RegistroView,CrearUsuarioView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('logout/', LogoutView.as_view(), name='custom_logout'),
    path('crear-usuario/', CrearUsuarioView.as_view(), name='crear_usuario'),
    path('registro/', RegistroView.as_view(), name='registro'),  #usuario registro
]
