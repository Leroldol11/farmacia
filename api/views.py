from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Usuario, Empleado, Proveedor, Cliente,
    CategoriaProducto, Producto, InventarioLote,
    Compra, DetalleCompra, Venta, DetalleVenta
)
from .serializers import (
    UsuarioSerializer, EmpleadoSerializer, ProveedorSerializer, ClienteSerializer,
    CategoriaProductoSerializer, ProductoSerializer, InventarioLoteSerializer,
    CompraSerializer, DetalleCompraSerializer, VentaSerializer, DetalleVentaSerializer
)

from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    permission_classes = [IsAuthenticated]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class InventarioLoteViewSet(viewsets.ModelViewSet):
    queryset = InventarioLote.objects.all()
    serializer_class = InventarioLoteSerializer
    permission_classes = [IsAuthenticated]

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer
    permission_classes = [IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    permission_classes = [IsAuthenticated]
