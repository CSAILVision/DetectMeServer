from django.views.generic import TemplateView
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from leaderboards import views, views_api


# Patters for the API access.
urlpatterns = patterns(
    '',
    # post of the detector performance
    url(r'^api/performance/$',
        views_api.PerformanceAPICreate.as_view()),
)

# Add suffix to nice access to the detectors.
urlpatterns = format_suffix_patterns(urlpatterns)


# Patterns for the normal access.
urlpatterns += patterns(
    '',
    url(r'^$', views.competition_detail, name="competition_detail"),
    url(r'^(?P<category>\w+)$', views.show_leaderboard, name='leaderboard'),
)