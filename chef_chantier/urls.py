from chef_chantier import views
from django.conf.urls import url 

urlpatterns = [

    url(r'^missions$', views.missions),
    url(r'^missions/detail$', views.mission_detail),


]