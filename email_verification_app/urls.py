# email_verification_app/api/urls.py
from django.urls import path
from .views import verify_email

urlpatterns = [
    path("verify_email/", verify_email, name="verify_email"),
]
