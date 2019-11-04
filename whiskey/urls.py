from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', all_whiskeys, name='whiskeys'),
    url(r'whiskey/(\d+)', get_whiskey, name='whiskey'),
    url(r'^distiller/(\d+)', get_distiller, name='distiller'),
    url(r'^add_whiskey/', add_whiskey, name='addwhiskey'),
    url(r'^add_distiller/', add_distiller, name='adddistiller'),

]