# Converts all the elements of the database to 2 point precision


from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib.auth.models import User
import settings
from detectors.models import Detector
import json

import simplejson

class PrettyFloat(float):
    def __repr__(self):
        return '%.2g' % self


def pretty_floats(obj):
    if isinstance(obj, float):
        return PrettyFloat(obj)
    elif isinstance(obj, dict):
        return dict((k, pretty_floats(v)) for k, v in obj.items())
    elif isinstance(obj, (list, tuple)):
        return map(pretty_floats, obj)             
    return obj


setup_environ(settings)

detectors = Detector.objects.all()

for detector in detectors:
    print detector.name + ' - ' +str(detector.pk)
    weights = json.loads(detector.weights)
    detector.weights = json.dumps(pretty_floats(weights))

    svs  = json.loads(detector.support_vectors)
    detector.support_vectors = json.dumps(pretty_floats(svs))

    detector.save()