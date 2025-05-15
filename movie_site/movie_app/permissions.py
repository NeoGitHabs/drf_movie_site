from rest_framework import permissions


class CheckRole(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'pro':
            return True
        return False

