
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsExperienceOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change experiences."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )
