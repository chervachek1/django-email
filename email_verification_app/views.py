import datetime
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import EmailVerificationResult
from .utils.email_client import verification_client


@csrf_exempt
def verify_email(request: WSGIRequest) -> HttpResponse:
    form_errors = None
    if request.method == "PUT":
        print(request.body)
    if request.method == "POST":
        email = request.POST.get("email")
        email_obj = EmailVerificationResult.objects.filter(email=email).first()
        response = verification_client.email_verifier(email)
        status = response.get("data", {}).get("status", None)
        if status:
            if email_obj:
                email_obj.status = status
                email_obj.created_at = datetime.datetime.now().astimezone(
                    datetime.timezone.utc
                )
                email_obj.save()
            else:
                EmailVerificationResult.objects.create(email=email, status=status)
        else:
            form_errors = [error for error in response.get("errors", [])]
    emails = EmailVerificationResult.objects.all()
    return render(
        request, "email_list.html", {"emails": emails, "form_errors": form_errors}
    )


def delete_email(request: WSGIRequest, email_id: int) -> HttpResponse:
    email = EmailVerificationResult.objects.get(pk=email_id)
    email.delete()
    return redirect("verify_email")
