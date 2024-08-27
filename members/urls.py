from django.urls import path
from .views import UserRegister, LoginPage

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),  # Add login URL
]
