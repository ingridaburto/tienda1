from rest_framework import serializers
from tien import models


class Clientes(serializers.ModelSerializer):
    class Meta:
        fields = (
            'nombre',
            'direccion',
            'telefono',

             )


class Factura(serializers.ModelSerializer):
    class Meta:
        fields = (
            'fecha',
            'IDCliente',
        )


class Categoria(serializers.ModelSerializer):
    class Meta:
        fields = (
            'descripcion',
        )


class Proveedor(serializers.ModelSerializer):
    class Meta:
        fields = (
            'nombre',
            'direccion',
            'telefono',
        )


class Producto(serializers.ModelSerializer):
    class Meta:
        fields = (
            'descripcion',
            'precio',
            'IDCategoria',
            'IDProveedor',
        )


class Ventas(serializers.ModelSerializer):
    class Meta:
        fields = (
            'IDFactura',
            'IDProducto',
            'cantidad',
        )