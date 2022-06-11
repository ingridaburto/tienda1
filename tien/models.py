from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    direccion = models.CharField(verbose_name='Dirección', max_length=150)
    telefono = models.CharField(verbose_name='Teléfono', max_length=20)

    def _str_(self):
        return "Nombre: {0} -> Teléfono: {1} -> Dirrección: {2}".format(self.nombre,self.telefono,self.direccion)


class Factura(models.Model):
    fecha = models.DateField(verbose_name='Fecha', max_length=10)
    IDCliente = models.ForeignKey(Clientes, verbose_name='Cliente', on_delete=models.CASCADE)

    def _str_(self):
        return "Cliente: {0} -> Factura: {1}".format(self.IDCliente,self.fecha)


class Categoria(models.Model):
    descripcion = models.CharField(verbose_name='Descripción', max_length=150)

    def _str_(self):
        return self.descripcion


class Proveedor(models.Model):
    nombre = models.CharField(verbose_name='Nombre',max_length=150,unique=True)
    direccion = models.CharField(verbose_name='Dirección',max_length=150)
    telefono = models.CharField(verbose_name='Teléfono',max_length=20)

    def _str_(self):
        return "Teléfono: {0} -> Proveedor: {1}".format(self.nombre,self.direccion,self.telefono)


class Producto(models.Model):
    descripcion = models.CharField(verbose_name='Descripción', max_length=150)
    precio = models.DecimalField(verbose_name='Precio', decimal_places=2,max_digits=80,default=0.00)
    IDCategoria = models.ForeignKey(Categoria, verbose_name='Categoria',on_delete=models.CASCADE)
    IDProveedor = models.ForeignKey(Proveedor,verbose_name='Proveedor',on_delete=models.CASCADE)

    def _str_(self):
        return self.descripcion


class Ventas(models.Model):
    IDFactura = models.ForeignKey(Factura,verbose_name='Factura',on_delete=models.CASCADE)
    IDProducto = models.ForeignKey(Producto, verbose_name='Producto',on_delete=models.CASCADE)
    cantidad = models.CharField(verbose_name='Cantidad', max_length=50)

    def _str_(self):
        return "Factura: {0} -> Producto: {1}".format(self.IDFactura,self.IDProducto,self.cantidad)