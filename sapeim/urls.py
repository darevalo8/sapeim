from django.conf.urls import url
from sapeim import views
from sapeim.views import AddElement, IndexView, UpdateElement, DeleteElement
from sapeim.views import ListBland, AddBland, DeleteBland, ListPrestamo, DetailPrestamo
from sapeim.views import ListElementType, AddElementType, DeleteElementType

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^add-elemento$', AddElement.as_view(), name='add-elemento'),
    url(r'^update-elemento/(?P<pk>\d+)$', UpdateElement.as_view(), name='up-elemento'),
    url(r'^delete-elemento/(?P<pk>\d+)$', DeleteElement.as_view(), name='delete-elemento'),
    url(r'^list-bland$', ListBland.as_view(), name='listar-marca'),
    url(r'^add-bland$', AddBland.as_view(), name='add-bland'),
    url(r'^delete-bland/(?P<pk>\d+)$', DeleteBland.as_view(), name='delete-bland'),
    url(r'^list-type$', ListElementType.as_view(), name='listar-tipoE'),
    url(r'^add-type$', AddElementType.as_view(), name='add-tipoE'),
    url(r'^delete-type/(?P<pk>\d+)$', DeleteElementType.as_view(), name='delete-tipoE'),
    url(r'^registro$', views.registro, name='registro'),
    url(r'^prestamos$', ListPrestamo.as_view(), name='list-prestamo'),
    url(r'^add-prestamo$', views.prestamo, name='add_prestamo'),
    url(r'^detail-prestamo/(?P<pk>\d+)$', DetailPrestamo.as_view(), name='detalle-pr'),
    url(r'^devoluciones/(?P<pk>\d+)$', views.devolucion, name='devoluciones'),
]
