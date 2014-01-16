from django.forms import ModelForm, RadioSelect
from .models import AbuseReport


class AbuseReportForm(ModelForm):
    class Meta:
        model = AbuseReport
        fields = ['abuse_type', ]
        widgets = {'abuse_type': RadioSelect}
