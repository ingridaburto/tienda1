from django.urls import include, path
from rest_framework import routers
from tien import views

router = routers.DefaultRouter()
router.register(r'Clientes', views.Clientes)
router.register(r'Factura', views.Factura)
router.register(r'Categoria', views.Categoria)
router.register(r'Proveedor', views.Proveedor)
router.register(r'Producto', views.Producto)
router.register(r'Ventas', views.Ventas)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('views.Clientes', include('rest_framework.urls', namespace='Clientes')),
    path('views.Factura', include('rest_framework.urls', namespace='Factura')),
    path('views.Categoria', include('rest_framework.urls', namespace='Categoria')),
    path('views.Proveedor', include('rest_framework.urls', namespace='Proveedor')),
    path('views.Producto', include('rest_framework.urls', namespace='Producto')),
    path('views.Ventas', include('rest_framework.urls', namespace='Ventas')),

]