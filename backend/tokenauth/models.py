from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from rest_framework.authtoken.models import Token
import uuid


# Replace the default User model with a custom one
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class ExpiringToken(Token):
    expiration = models.DateTimeField(null=True)

    def has_expired(self):
        return self.expiration < timezone.now()

    def save(self, *args, **kwargs):
        if not self.expiration:
            self.expiration = timezone.now() + timezone.timedelta(minutes=5)
            # self.expiration = timezone.now() + timezone.timedelta(seconds=30)
        super(ExpiringToken, self).save(*args, **kwargs)
