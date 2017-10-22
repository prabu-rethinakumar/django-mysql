from django.conf.urls import url
from . import views


app_name = 'firstapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[a-z]+)/test/$', views.test, name='test'),
    url(r'^(?P<name>[aA-zZ]+)/details/$', views.details, name='details'),
]

