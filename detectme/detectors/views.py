from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Detector 




class DetectorList(ListView):
    model = Detector
    context_object_name = 'detector_list'
    template_name = 'detectors/detector_list'

    def get_queryset(self):
        return (Detector.objects
                .filter(get_allowed_detectors(self.request.user))
                .order_by('-created_at'))


class DetectorDetail(DetailView):
    model = Detector
    template_name = 'detectors/detector_detail'
    context_object_name = 'detector'

    def get_queryset(self):
        qs = super(DetectorDetail, self).get_queryset()
        return qs.filter(get_allowed_detectors(self.request.user))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetectorDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['annotatedimage_list'] = self.object.annotatedimage_set.all()
        return context


def get_allowed_detectors(user):
    """
    Query only detectors not deleted and (public or private if I am the owner)
    """
    if user.is_authenticated():
        return ((Q(author=user.get_profile()) | Q(is_public=True)) &
                Q(is_deleted=False))
    else:
        return (Q(is_public=True) &
                Q(is_deleted=False))

