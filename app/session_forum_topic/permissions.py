from rest_framework import permissions


class SessionForumTopicPermission(permissions.BasePermission):
    message = 'User not allowed.'

    def has_permission(self, request, view):

        account_type = request.user.user_type

        if request.method == 'GET':
            can_get = ['AT', 'SP', 'AD']
            return account_type in can_get

        elif request.method == 'POST':
            can_create = ['AD', 'SP']
            return account_type in can_create

        elif request.method == 'PUT':
            can_update = ['AD', 'SP']
            return account_type in can_update

        elif request.method == 'DELETE':
            can_delete = ['AD', 'SP']
            return account_type in can_delete

        else:
            return False