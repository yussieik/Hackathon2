from django.contrib import admin

# Register your models here.
from .models import UserProfile, Donation
admin.site.register(UserProfile)
admin.site.register(Donation)