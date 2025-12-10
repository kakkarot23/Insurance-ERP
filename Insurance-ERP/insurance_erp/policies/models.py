from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

class Policy(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('SUSPENDED', 'Suspended'),
        ('EXPIRED', 'Expired'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    POLICY_TYPES = [
        ('LIFE', 'Life Insurance'),
        ('HEALTH', 'Health Insurance'),
        ('AUTO', 'Auto Insurance'),
        ('PROPERTY', 'Property Insurance'),
        ('MARINE', 'Marine Insurance'),
    ]
    
    policy_number = models.CharField(max_length=50, unique=True)
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES)
    holder_name = models.CharField(max_length=255)
    holder_email = models.EmailField()
    holder_phone = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    premium_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    sum_insured = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    coverage_details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='policies_created')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Policy'
        verbose_name_plural = 'Policies'

    def __str__(self):
        return f"{self.policy_number} - {self.holder_name}"


class PremiumCalculation(models.Model):
    policy = models.OneToOneField(Policy, on_delete=models.CASCADE, related_name='premium_calc')
    base_premium = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    risk_factor = models.DecimalField(max_digits=5, decimal_places=3, default=1.0)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=18.0)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total_premium = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    calculated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Premium Calculation'
        verbose_name_plural = 'Premium Calculations'

    def __str__(self):
        return f"Premium Calc - {self.policy.policy_number}"

    def calculate_total(self):
        """Calculate total premium with tax and discount"""
        taxable = self.base_premium * self.risk_factor
        tax = taxable * (self.tax_rate / 100)
        discount = (taxable + tax) * (self.discount_percentage / 100)
        self.total_premium = taxable + tax - discount
        return self.total_premium
