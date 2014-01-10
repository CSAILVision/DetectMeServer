from django.conf.urls import patterns, url
from django.contrib.auth.views import password_reset
from django.views.decorators.csrf import csrf_exempt
from userena import settings as userena_settings
from accounts import views


# Create a new user over the api
urlpatterns = patterns(
    '',
    url(r'^create/$', views.AccountAPICreate.as_view()),
    url(r'^detail/(?P<username>\w+)/$', views.AccountAPIDetail.as_view()), 
)
