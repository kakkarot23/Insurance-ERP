from django.db import models
from django.contrib.auth.models import User
from claims.models import Claim
from policies.models import Policy

class FraudRisk(models.Model):
    RISK_LEVEL = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('FLAGGED', 'Flagged'),
        ('UNDER_INVESTIGATION', 'Under Investigation'),
        ('CONFIRMED', 'Confirmed Fraud'),
        ('CLEARED', 'Cleared'),
        ('CLOSED', 'Closed'),
    ]

    claim = models.OneToOneField(Claim, on_delete=models.CASCADE, related_name='fraud_risk', null=True, blank=True)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='fraud_risks')
    risk_score = models.IntegerField(default=0)  # 0-100
    risk_level = models.CharField(max_length=20, choices=RISK_LEVEL, default='LOW')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='FLAGGED')
    
    # Red Flags
    is_duplicate_claim = models.BooleanField(default=False)
    is_over_claim = models.BooleanField(default=False)
    is_staged_claim = models.BooleanField(default=False)
    unusual_pattern = models.BooleanField(default=False)
    high_claim_frequency = models.BooleanField(default=False)
    
    description = models.TextField()
    investigation_notes = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-risk_score']

    def __str__(self):
        return f"Fraud Risk - {self.policy.policy_number} - {self.risk_level}"

    def calculate_risk_score(self):
        """Calculate fraud risk score based on flags"""
        score = 0
        if self.is_duplicate_claim:
            score += 30
        if self.is_over_claim:
            score += 25
        if self.is_staged_claim:
            score += 35
        if self.unusual_pattern:
            score += 20
        if self.high_claim_frequency:
            score += 15
        
        self.risk_score = min(score, 100)
        
        if self.risk_score < 30:
            self.risk_level = 'LOW'
        elif self.risk_score < 50:
            self.risk_level = 'MEDIUM'
        elif self.risk_score < 80:
            self.risk_level = 'HIGH'
        else:
            self.risk_level = 'CRITICAL'
        
        return self.risk_score
