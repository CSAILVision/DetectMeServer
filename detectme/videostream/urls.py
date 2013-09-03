from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import box_list, box_detail, box_last

urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name='videostream/stream.html')), 
    												name="videostream"),
    url(r'^boxes/last/(?P<timestamp>\d+)/$', box_last),
    url(r'^boxes/$', box_list),
    url(r'^boxes/(?P<pk>[0-9]+)/$', box_detail),
)


