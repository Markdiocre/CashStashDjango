from rest_framework import permissions

# class AdminLevelOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         print(request.user.user_level)
#         if request.user.user_level.group_level == 1:
#             return True
#         else:
#             return False

class CurrentUserOrAdminLevel(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)