import django
from codesolid_demo.config import get_config
from django.contrib.auth import get_user_model

django.setup()
User = get_user_model()
superusers = User.objects.filter(is_superuser=True)
if len(superusers) == 0:
    user_name = get_config("DJANGO_SUPERUSER")
    user_email = get_config("DJANGO_SUPERUSER_EMAIL")
    user_password = get_config("DJANGO_SUPERUSER_PASSWORD")
    User.objects.create_superuser(user_name, user_email, user_password)
