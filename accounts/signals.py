import hashlib
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile
# from datetime import datetime, timedelta
# from django.conf import settings


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.activation_key = hashlib.sha1(str(user).encode("utf-8")).hexdigest()
        # profile.key_expires = datetime.now() + timedelta(days=settings.KEY_EXPIRES_DAYS)
        profile.save()
