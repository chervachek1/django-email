from django.urls import path
from .views import verify_email, delete_email

urlpatterns = [
    path("verify_email/", verify_email, name="verify_email"),
    path("delete_email/<str:email_id>/", delete_email, name="delete_email"),
]
