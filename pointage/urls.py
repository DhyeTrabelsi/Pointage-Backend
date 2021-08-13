
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^employes/', include('employes.urls')),
    url(r'^chef/chantier/', include('chef_chantier.urls')),

]
urlpatterns += staticfiles_urlpatterns()
