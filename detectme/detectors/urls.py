from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from detectors import views


# Patters for the API access.
urlpatterns = patterns(
    '',
    url(r'^api/$', views.DetectorAPIList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.DetectorAPIDetail.as_view()),
    # url(r'^api/(?P<pk>[0-9]+)/delete/$', views.deletDetector),
    url(r'^api/annotatedimages/$', views.AnnotatedImageAPIList.as_view()),
    url(r'^api/annotatedimages/(?P<pk>[0-9]+)/$', views.AnnotatedImageAPIDetail.as_view()),
)

# Add suffix to nice access to the detectors.
urlpatterns = format_suffix_patterns(urlpatterns)


# Include the login and logout views for the browsable API.
urlpatterns += patterns(
    '',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)




# Patterns for the normal access.
urlpatterns += patterns(
    '',
    url(r'^$', views.DetectorList.as_view(), name='detector_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetectorDetail.as_view(), name='detector_detail')
)
