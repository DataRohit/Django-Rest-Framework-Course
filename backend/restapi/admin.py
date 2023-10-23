from django.contrib import admin
from restapi.models import User, ExpiringToken

# Register your models here.
admin.site.register(User)
admin.site.register(ExpiringToken)
