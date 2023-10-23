from rest_framework import permissions
from tokenauth.permissions import *


class TokenEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsTokenEditorPermission]


class ProductEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsProductEditorPermission]
