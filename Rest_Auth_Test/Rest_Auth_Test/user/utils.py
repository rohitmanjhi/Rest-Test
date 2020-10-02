
from Rest_Auth_Test.user.models import User


class Permission:
    def __init__(self, user):
        self.user = user
        self.group = user.groups.first()

    # Get users data after check role of user
    def get_permission(self):
        msg = None
        if self.group.name == "Student":
            return User.objects.all(), msg
        if self.group.name == "Teacher":
            return User.objects.all(), msg
        if self.group.name == "Super-admin":
            return User.objects.all(), msg

    # Delete users data after check role of user
    def delete_permission(self):
        msg = None
        if self.group.name == "Student":
            msg = "Permission Denied"
            return None, msg
        if self.group.name == "Teacher":
            msg = "Permission Denied"
            return None, msg
        if self.group.name == "Super-admin":
            return User.objects.all(), msg

    # Update users data after check role of user
    def update_permission(self, user):
        msg = None
        if self.group.name == "Student":
            msg = "Permission Denied"
            return None, msg
        if self.group.name == "Teacher":
            if user.groups.first().name == "Student":
                return user, msg
            msg = "Permission Denied"
            return None, msg
        if self.group.name == "Super-admin":
            return user, msg
