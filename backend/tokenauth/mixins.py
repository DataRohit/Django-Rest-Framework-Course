from rest_framework import permissions
from tokenauth.permissions import *


class ProductEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsProductEditorPermission]
