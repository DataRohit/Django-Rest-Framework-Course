from rest_framework import permissions
from restapi.permissions import *


class TokenEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsTokenEditorPermission]


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
