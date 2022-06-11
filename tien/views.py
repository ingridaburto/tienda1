from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tien.serializers import Clientes, Factura, Categoria, Proveedor, Producto, Ventas


class Clientes(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = Clientes
    permission_classes = [permissions.IsAuthenticated]


class Factura(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Factura
    permission_classes = [permissions.IsAuthenticated]


class Categoria(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Categoria
    permission_classes = [permissions.IsAuthenticated]


class Proveedor(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Proveedor
    permission_classes = [permissions.IsAuthenticated]


class Producto(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Producto
    permission_classes = [permissions.IsAuthenticated]


class Ventas(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Ventas
    permission_classes = [permissions.IsAuthenticated]