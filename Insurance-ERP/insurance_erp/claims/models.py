from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from policies.models import Policy

class Claim(models.Model):
    STATUS_CHOICES = [
        ('FILED', 'Filed'),
        ('UNDER_REVIEW', 'Under Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('PAID', 'Paid'),
    ]
    
    claim_number = models.CharField(max_length=50, unique=True)
    policy = models.ForeignKey(Policy, on_delete=models.PROTECT, related_name='claims')
    claim_date = models.DateField()
    incident_date = models.DateField()
    claim_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='FILED')
    approved_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    rejection_reason = models.TextField(blank=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='claims_assigned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.claim_number} - {self.policy.policy_number}"


class ClaimDocument(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=100)
    file = models.FileField(upload_to='claim_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.claim.claim_number} - {self.document_type}"
