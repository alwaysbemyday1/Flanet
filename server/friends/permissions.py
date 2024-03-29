from rest_framework.permissions import BasePermission

class IsUser(BasePermission):

    def has_object_permission(self, request, view, user):
        return user == request.user