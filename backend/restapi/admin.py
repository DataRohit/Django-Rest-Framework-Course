from django.contrib import admin
from restapi.models import User, ExpiringToken

# Register your models here.
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff")


class ExpiringTokenAdmin(admin.ModelAdmin):
    list_display = ("key", "user", "expiration")


admin.site.register(User, UserAdmin)
admin.site.register(ExpiringToken, ExpiringTokenAdmin)
