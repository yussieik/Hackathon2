from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import RegisterForm, DonationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import UserProfile, Donation

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
    
def home_view(request):
    return render(request, 'home.html')

def create_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
            return redirect('list')
    else:
        form = DonationForm()
    return render(request, 'create_donation.html', {'form': form})

def list_donations(request):
    donations = Donation.objects.filter(user=request.user)
    return render(request, 'list_donations.html', {'donations': donations})

def my_program_view(request):
    return render(request, 'my_program.html')