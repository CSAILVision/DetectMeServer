from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import box_list, box_detail, box_last

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='videostream/stream.html'), name="videostream"),
    url(r'^boxes/last/(?P<timestamp>\d+)/$', box_last),
    url(r'^boxes/$', box_list),
    url(r'^boxes/(?P<pk>[0-9]+)/$', box_detail),

)


# urlpatterns = patterns('snippets.views',
#     url(r'^snippets/$', 'snippet_list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
# )
