from django.urls import path, include
from .views import IndexPage

app_name = 'home_page'

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
]