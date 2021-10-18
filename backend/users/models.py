from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from fcm_django.models import FCMDevice


def profile_image_path(instance, filename):
    return f'users_photos/{filename}'


class User(AbstractUser):
    first_name = models.CharField(
        _('first name'), max_length=50
    )
    last_name = models.CharField(_(
        'last name'), max_length=150
    )
    photo = models.ImageField(
        _('Photo'),
        default='',
        upload_to=profile_image_path
    )
    phone = models.CharField(
        _("Phone"),
        blank=True,
        null=True,
        max_length=255
    )
    age = models.PositiveSmallIntegerField(
        _("Age"),
        blank=True,
        null=True
    )
    height = models.PositiveSmallIntegerField(
        _("height"),
        blank=True,
        null=True,
    )
    weight = models.PositiveSmallIntegerField(
        _("Weight"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True


@receiver(post_save, sender=FCMDevice)
def send_test_notification(sender, instance, **kwargs):
    instance.send_message(
        title='Test notification',
        body='All good! Device is registered'
    )
