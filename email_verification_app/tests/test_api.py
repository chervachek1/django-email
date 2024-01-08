from django.test import TestCase, Client
from email_verification_app.models import EmailVerificationResult


class MyAPITestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.email = "test_for_delete@gmail.com"

    def test_verify_email_post_success(self) -> None:
        email = "test@gmail.com"
        response = self.client.post("/emails/verify_email/", {"email": email})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(EmailVerificationResult.objects.filter(email=email).exists())

    def test_verify_email_post_failure(self) -> None:
        invalid_email = "invalid_email"
        response = self.client.post("/emails/verify_email/", {"email": invalid_email})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context.get("form_errors"))
        self.assertFalse(
            EmailVerificationResult.objects.filter(email=invalid_email).exists()
        )

    def test_verify_email_get(self) -> None:
        response = self.client.get("/emails/verify_email/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("emails", response.context)
        self.assertIn("form_errors", response.context)

    def test_delete_verify_result(self) -> None:
        result = EmailVerificationResult.objects.create(
            email=self.email, status="valid"
        )
        response = self.client.get(f"/emails/delete_email/{result.id}/")
        result = EmailVerificationResult.objects.filter(pk=result.id).first()
        self.assertIsNone(result)
