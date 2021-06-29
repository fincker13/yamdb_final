from rest_framework import permissions


class IsSuperUserOrAdminOnly(permissions.BasePermission):
    """permission определяет права суперадминистратора или админа"""
    message = 'У вас недостаточно прав.'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    """permission определяет права администратора или только на чтение"""
    message = 'У вас недостаточно прав.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            return request.user.is_authenticated

        return request.user.is_admin or request.user.is_moderator


class IsModeratorOrOwnerOrReadOnly(permissions.BasePermission):
    message = 'У вас недостаточно прав.'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return request.user.is_moderator or obj.author == request.user


class IsStaffOrOwnerOrReadOnly(permissions.BasePermission):
    """permission определяет staff, owner или readonly"""
    message = 'У вас недостаточно прав.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (request.user.is_admin
                or request.user.is_moderator
                or request.user == obj.author)
