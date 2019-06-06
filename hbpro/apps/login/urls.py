from django.conf.urls import url

from apps.login.views import login

urlpatterns = [
    url(r'^$', login, name='login'),
]
