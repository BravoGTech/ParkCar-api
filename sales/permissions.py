from rest_framework import permissions
import ipdb


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" and request.user.is_authenticated:
            return True

        return (request.user.is_superuser and request.user.is_authenticated)
