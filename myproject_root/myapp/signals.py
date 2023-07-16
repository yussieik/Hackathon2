from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import UserProfile

#User -> post save signal -> revceiver function -> new UserProfile
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        UserProfile.objects.create(user = instance)
        
        if not instance.is_staff:
            group = Group.objects.djaget(name='regular')
            instance.groups.add(group)
 
@receiver(post_save, sender = User)           
def attach_user_group(sender, instance, created, **kwargs):
    if created :
         if not instance.is_staff:
            group = Group.objects.get(name='regular')
            instance.groups.add(group)
    else :
        if instance.is_staff:
            group = Group.objects.get(name='regular')
            group.user_set.remove(instance)