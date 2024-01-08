from django.db import models


class EmailVerificationResult(models.Model):
    email = models.EmailField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.email} - {self.status}"
