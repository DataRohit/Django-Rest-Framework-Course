from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token


class ExpiringToken(Token):
    expiration = models.DateTimeField(null=True)

    def has_expired(self):
        return self.expiration < timezone.now()

    def save(self, *args, **kwargs):
        if not self.expiration:
            self.expiration = timezone.now() + timezone.timedelta(minutes=2)
        super(ExpiringToken, self).save(*args, **kwargs)
