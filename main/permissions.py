
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        user = request.user

        # Semua orang boleh membaca data
        if request.method in SAFE_METHODS:
            return True

        # Superuser boleh melakukan semua perubahan
        if user.is_superuser:
            return True

        # Pengunjung dan pengguna biasa tidak boleh mengubah data
        if not user.is_authenticated:
            return False

        # Editor hanya boleh PUT dan PATCH
        if request.method in ["PUT", "PATCH"]:
            return user.groups.filter(name="Editor").exists()

        # POST dan DELETE hanya untuk superuser
        return False
