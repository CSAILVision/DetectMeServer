from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from detectors import views, views_api


# Patters for the API access.
urlpatterns = patterns(
    '',
    url(r'^api/$',
        views_api.DetectorAPIList.as_view()),
    
    # get detectors uploaded later than time
    url(r'^api/lastupdated/(?P<time>[0-9]+)/$',
        views_api.DetectorAPITimeList.as_view()),

    url(r'^api/(?P<pk>[0-9]+)/$',
        views_api.DetectorAPIDetail.as_view()),
    
    url(r'^api/annotatedimages/$',
        views_api.AnnotatedImageAPIList.as_view()),
    
    url(r'^api/annotatedimages/(?P<pk>[0-9]+)/$',
        views_api.AnnotatedImageAPIDetail.as_view()),
    
    url(r'^api/annotatedimages/fordetector/(?P<detector>[0-9]+)/$',
        views_api.AnnotatedImagesForDetector.as_view()),

    url(r'^api/supportvectors/(?P<pk>[0-9]+)/$',
        views_api.SupportVectorsForDetector.as_view()),
    
    url(r'^api/ratings/$',
        views_api.RatingAPIList.as_view()),

    url(r'^api/report/$', 
        views_api.AbuseReportAPICreate.as_view()),
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
    url(r'^(?P<pk>[0-9]+)/$', views.DetectorDetail.as_view(), name='detector_detail'),
    url(r'^report/(?P<detector_pk>[0-9]+)/$', views.report_view, name='report_view'),
)
