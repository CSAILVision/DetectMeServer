from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from .models import Detector, AbuseReport
from .forms import AbuseReportForm


class DetectorList(ListView):
    model = Detector
    context_object_name = 'detector_list'
    template_name = 'detectors/detector_list'

    def get_queryset(self):
        queryset = (Detector.objects
                    .filter(get_allowed_detectors(self.request.user))
                    .order_by('-created_at'))

        if 'q' in self.request.GET:
            search_term = self.request.GET['q']
            queryset = queryset.filter(name__contains=search_term)
    
        return queryset


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
        context['report_form'] = AbuseReportForm()

        # Add reported message
        if self.request.user.is_authenticated():
            detector = self.get_object()
            profile = self.request.user.get_profile()
            r = AbuseReport.objects.filter(detector=detector, author=profile)
            if r:
                messages.add_message(self.request, messages.ERROR, 'You have reported this detector for abuse.')
        return context


def report_view(request, detector_pk):
    """
    Handles the validation of the abuse report form
    """
    if request.POST:
        report = AbuseReport(author=request.user.get_profile(),
                             detector=Detector.objects.get(pk=detector_pk))
        print report
        form = AbuseReportForm(request.POST, instance=report)
        if form.is_valid():
            report = form.save()
            return HttpResponseRedirect(reverse('detector_detail', args=(detector_pk,)))


def get_allowed_detectors(user):
    """
    Query only detectors not deleted and (public or private if I am the owner)
    """
    if user.is_authenticated():
        if user.is_staff:
            return Q(is_deleted=False)
        else:
            return ((Q(author=user.get_profile()) | Q(is_public=True)) &
                    Q(is_deleted=False))
    else:
        return (Q(is_public=True) &
                Q(is_deleted=False))
