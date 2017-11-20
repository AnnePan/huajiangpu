from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_goods/$', views.add_goods, name='add_goods'),
]
