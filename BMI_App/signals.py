from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a UserProfile whenever a new User is created.
    """
    if created:  # Only create a profile if this is a new user
        UserProfile.objects.create(user=instance)
        print(f"UserProfile created for {instance.email}")
