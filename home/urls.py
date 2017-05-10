from django.conf.urls import include, url
from home.views import *


urlpatterns = [
    url(
        r'^$',
        Home.as_view(),
        name='home'),
]