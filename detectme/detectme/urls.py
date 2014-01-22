from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^detectors/', include('detectors.urls')),
    url(r'^leaderboard/', include('leaderboards.urls')),
    url(r'^videostream/', include('videostream.urls')),
    url(r'^how_it_works/$', TemplateView.as_view(template_name='how_it_works.html'),
        name="how_it_works"),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),
        name="about"),

    # create account over api
    (r'^accounts/api/', include('accounts.urls')),

    # userena app
    (r'^accounts/', include('userena.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Include the login and logout views for the API.
urlpatterns += patterns('',
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
)

# Django Time profiler
urlpatterns += patterns('',
    url(r'^profiler/', include('profiler.urls'))
)

# Allow access to the Media folder from the browser
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
            }),
    )
