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

    url(r'^password/reset/$', csrf_exempt(password_reset),
       {'template_name': 'userena/password_reset_form.html',
        'email_template_name': 'userena/emails/password_reset_message.txt',
        'extra_context': {'without_usernames': userena_settings.USERENA_WITHOUT_USERNAMES}},
       name='userena_password_reset_mobile'),
)
