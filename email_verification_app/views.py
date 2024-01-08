from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import EmailVerificationResult
from .utils.email_client import verification_client


@csrf_exempt
def verify_email(request: WSGIRequest) -> HttpResponse:
    form_errors = None
    if request.method == "POST":
        email = request.POST.get("email")
        if not EmailVerificationResult.objects.filter(email=email).exists():
            response = verification_client.email_verifier(email)
            status = response.get("data", {}).get("status", None)
            if status:
                EmailVerificationResult.objects.create(email=email, status=status)
            else:
                form_errors = [error for error in response.get("errors", [])]
    emails = EmailVerificationResult.objects.all()
    return render(
        request, "email_list.html", {"emails": emails, "form_errors": form_errors}
    )
