from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^silly/$', views.sillyMessage, name='index'),
]
