from django.urls import path
from .views import home_view
from django.contrib.auth import views
from .views import register, create_donation, list_donations, my_program_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('register/', register, name = 'register'),
    path('home', home_view, name='home'),
    path('create/', create_donation, name='create'),
    path('list/', list_donations, name='list'),
    path('my-template/', my_program_view, name='my-program'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)