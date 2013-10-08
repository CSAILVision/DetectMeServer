from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


class DetectMeProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique = True,
                                verbose_name = _('user'),
                                related_name = 'my_profile')
    
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
