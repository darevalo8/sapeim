from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('sapeim.urls', namespace="sapeim")),
    url(r'^admin/', include(admin.site.urls)),
]
