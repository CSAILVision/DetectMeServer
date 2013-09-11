from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from detectors import views


# Patters for the API access.
urlpatternsAPI = patterns(
    '',
    url(r'^api/$', views.DetectorAPIList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.DetectorAPIDetail.as_view()),
)

# Add suffix to nice access to the detectors.
urlpatterns = format_suffix_patterns(urlpatternsAPI)

# Patterns for the normal access.
urlpatterns = urlpatternsAPI + patterns(
    '',
    url(r'^$', views.DetectorList.as_view(), name='detector_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetectorDetail.as_view(), name='detector_detail')
)
