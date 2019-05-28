from django.conf.urls import url

from apps.register.views import index

urlpatterns = [
    url(r'^$',index, name='register'),
    
]
