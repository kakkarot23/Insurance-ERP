from django.db import models
from django.contrib.auth.models import User
import uuid

class KYCProfile(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('VERIFIED', 'Verified'),
        ('REJECTED', 'Rejected'),
        ('EXPIRED', 'Expired'),
    ]

    KYC_TYPE = [
        ('INDIVIDUAL', 'Individual'),
        ('CORPORATE', 'Corporate'),
        ('PARTNERSHIP', 'Partnership'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    kyc_type = models.CharField(max_length=20, choices=KYC_TYPE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    # Identity Documents
    identity_document_type = models.CharField(max_length=50)
    identity_document_number = models.CharField(max_length=100)
    identity_document_file = models.FileField(upload_to='kyc_documents/identity/')
    identity_verified_at = models.DateTimeField(null=True, blank=True)
    
    # Address
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='India')
    
    # Additional Documents
    address_proof_file = models.FileField(upload_to='kyc_documents/address/', null=True, blank=True)
    pan_card = models.CharField(max_length=20, blank=True)
    aadhar_number = models.CharField(max_length=20, blank=True)
    
    # Verification
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    verification_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'KYC Profile'
        verbose_name_plural = 'KYC Profiles'

    def __str__(self):
        return f"{self.full_name} - {self.status}"
