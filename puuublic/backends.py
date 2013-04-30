# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User

class EmailAuth(object):
    def authenticate(self, username=None, password=None):
        if not '@' in username:
            return None

        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


