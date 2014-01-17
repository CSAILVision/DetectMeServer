from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from userena.models import UserenaBaseProfile

from pybb.profiles import PybbProfile
# from annoying.fields import AutoOneToOneField
# from django.core.urlresolvers import reverse


class DetectMeProfile(UserenaBaseProfile, PybbProfile):
    user = models.OneToOneField(User,
                                unique = True,
                                verbose_name = _('user'),
                                related_name = 'detectme_profile')
    
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)

    @property
    def username(self):
        return self.user.username

    @property
    def num_annotated_images(self):
        return len(self.annotatedimage_set.all())

    @property
    def current_detectors(self):
        return self.detector_set.all().filter(is_deleted=False)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



# class Profile(PybbProfile):
#     """
#     Profile class that can be used if you doesn't have
#     your site profile.
#     """
#     user = AutoOneToOneField(User, related_name='pybb_profile', verbose_name=_('User'))

#     class Meta(object):
#         verbose_name = _('Profile')
#         verbose_name_plural = _('Profiles')

#     def get_absolute_url(self):
#         return reverse('pybb:user', kwargs={'username': getattr(self.user, username_field)})
