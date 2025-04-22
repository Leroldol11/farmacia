from rest_framework import routers
from .views import (
    UsuarioViewSet, EmpleadoViewSet, ProveedorViewSet, ClienteViewSet,
    CategoriaProductoViewSet, ProductoViewSet, InventarioLoteViewSet,
    CompraViewSet, DetalleCompraViewSet, VentaViewSet, DetalleVentaViewSet
)
from django.urls import path
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

urlpatterns = router.urls
