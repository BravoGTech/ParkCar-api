from rest_framework import permissions


class isAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser and request.method == "POST" or request.user.is_superuser and request.method == "GET"


class isAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_staff

