from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.g_list, name='list'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact_message, name='contact'),
]
