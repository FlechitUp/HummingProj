from django.conf.urls import url

from apps.login.views import index2

urlpatterns = [
    url(r'^$',index2),
    
]
