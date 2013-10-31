from django.conf.urls import patterns, url
from accounts import views


# Create a new user over the api
urlpatterns = patterns(
    '',
    url(r'^create/$', views.AccountAPICreate.as_view()),
    url(r'^update/(?P<username>\w+)/$', views.UserenaBaseProfileAPIUpdate.as_view()),
)
