from rest_framework import routers
from django.urls import path
from api.views import (
    UsuarioViewSet, EmpleadoViewSet, ProveedorViewSet, ClienteViewSet,
    CategoriaProductoViewSet, ProductoViewSet, InventarioLoteViewSet,
    CompraViewSet, DetalleCompraViewSet, VentaViewSet, DetalleVentaViewSet,
    LoginView, LogoutView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Rutas automáticas con router
router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('empleados', EmpleadoViewSet)
router.register('proveedores', ProveedorViewSet)
router.register('clientes', ClienteViewSet)
router.register('categorias', CategoriaProductoViewSet)
router.register('productos', ProductoViewSet)
router.register('inventarios', InventarioLoteViewSet)
router.register('compras', CompraViewSet)
router.register('detalle-compras', DetalleCompraViewSet)
router.register('ventas', VentaViewSet)
router.register('detalle-ventas', DetalleVentaViewSet)

# Rutas personalizadas (JWT y login/logout opcionales)
urlpatterns = [
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('login/', LoginView.as_view(), name='custom_login'),
    path('logout/', LogoutView.as_view(), name='custom_logout'),
]

# Agregar las rutas automáticas generadas por el router
urlpatterns += router.urls
