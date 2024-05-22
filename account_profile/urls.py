from django.urls import path
from account_profile import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]

