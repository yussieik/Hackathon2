from django.db import models
from datetime import date
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name= 'user_profile')
    
    
class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default = date.today)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Donation by {self.user.username}"