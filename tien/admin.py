from django.contrib import admin
from .models import Producto,Categoria,Proveedor

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)