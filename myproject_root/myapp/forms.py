from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Donation

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'telephone')
        
class DonationForm(forms.ModelForm):
    PAYMENT_METHOD_CHOICES = (
        ('cheque', 'Cheque'),
        ('bit', 'Bit'),
        ('cash', 'Cash'),
    )
    
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES)

    class Meta:
        model = Donation
        fields = ['amount', 'payment_method']
        widgets = {'date': forms.HiddenInput()}