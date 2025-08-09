from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsLibrarianOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.groups.filter(name='librarian').exists()

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.groups.filter(name='librarian').exists()