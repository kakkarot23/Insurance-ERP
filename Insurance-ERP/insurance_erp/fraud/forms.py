from django import forms
from .models import FraudRisk

class FraudRiskForm(forms.ModelForm):
    class Meta:
        model = FraudRisk
        fields = [
            'policy', 'claim', 'description',
            'is_duplicate_claim', 'is_over_claim', 'is_staged_claim',
            'unusual_pattern', 'high_claim_frequency'
        ]
        widgets = {
            'policy': forms.Select(attrs={'class': 'form-control'}),
            'claim': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_duplicate_claim': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_over_claim': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staged_claim': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'unusual_pattern': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'high_claim_frequency': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FraudInvestigationForm(forms.ModelForm):
    class Meta:
        model = FraudRisk
        fields = ['status', 'investigation_notes']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'investigation_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
