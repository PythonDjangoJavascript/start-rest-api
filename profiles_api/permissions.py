from rest_framework import permissions


class UpdateOwnProfele(permissions.BasePermission):
    """Allow user to edit their own proflie"""

    def has_object_permission(self, request, view, obj):
        """Check user  is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own staus"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
