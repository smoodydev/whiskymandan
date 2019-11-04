from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'user-review/(\d+)', get_review, name='userreview'),

]