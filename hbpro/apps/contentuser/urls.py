from django.conf.urls import url

from apps.contentuser.views import index, imdexTeam

urlpatterns = [
    url(r'^progress',index),
    url(r'^team', imdexTeam),
]
