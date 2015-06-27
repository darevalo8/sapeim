from django.conf.urls import url
from sapeim import views
from sapeim.views import AddElement, IndexView, UpdateElement, DeleteElement
from sapeim.views import ListBland, AddBland, DeleteBland

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^add-elemento$', AddElement.as_view(), name="add-elemento"),
    url(r'^update-elemento/(?P<pk>\d+)$', UpdateElement.as_view(), name="up-elemento"),
    url(r'^delete-elemento/(?P<pk>\d+)$', DeleteElement.as_view(), name="delete-elemento"),
    url(r'^list-bland$', ListBland.as_view(), name='listar-marca'),
    url(r'^add-bland$', AddBland.as_view(), name="add-bland"),
    url(r'^delete-bland/(?P<pk>\d+)$', DeleteBland.as_view(), name="delete-bland"),
    url(r'^registro$', views.registro, name='registro'),
    url(r'^prestamo$', views.prestamo, name='prestamo'),
]
