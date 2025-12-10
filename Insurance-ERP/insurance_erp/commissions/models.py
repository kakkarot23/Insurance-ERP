from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from policies.models import Policy

class Agent(models.Model):
    AGENT_TYPE = [
        ('INDIVIDUAL', 'Individual Agent'),
        ('AGENCY', 'Insurance Agency'),
        ('BROKER', 'Insurance Broker'),
    ]

    agent_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    agent_type = models.CharField(max_length=20, choices=AGENT_TYPE)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.agent_code} - {self.name}"


class Commission(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('PAID', 'Paid'),
        ('REVERSED', 'Reversed'),
    ]

    commission_number = models.CharField(max_length=50, unique=True)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name='commissions')
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='commissions')
    
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)
    base_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    commission_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    commission_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.commission_number} - {self.agent.name}"

    def calculate_commission(self):
        """Calculate commission amount based on rate"""
        self.commission_amount = self.base_amount * (self.commission_rate / 100)
        return self.commission_amount


class CommissionPayment(models.Model):
    PAYMENT_METHOD = [
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('CHECK', 'Check'),
        ('CASH', 'Cash'),
        ('OTHERS', 'Others'),
    ]

    payment_id = models.CharField(max_length=50, unique=True)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    payment_date = models.DateField()
    reference_number = models.CharField(max_length=100, blank=True)
    remarks = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-payment_date']

    def __str__(self):
        return f"{self.payment_id} - {self.commission.commission_number}"
