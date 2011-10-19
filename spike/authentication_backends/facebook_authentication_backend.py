from django.contrib.auth.models import User

class FacebookAuthenticationBackend:
    supports_anonymous_user = False
    supports_object_permissions = False

    def authenticate(self, username, email, facebook_name):
        try:
            user = User.objects.get(username = username)
            return user
        except:
            user = User.objects.create_user(username, email)
            user.first_name = facebook_name
            user.is_active = True
            user.save()
            
            return user
            
    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)
        except:
            return None
