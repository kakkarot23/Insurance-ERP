from django import forms
from .models import Policy, PremiumCalculation

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = [
            'policy_number', 'policy_type', 'holder_name', 'holder_email',
            'holder_phone', 'start_date', 'end_date', 'status',
            'premium_amount', 'sum_insured', 'coverage_details'
        ]
        widgets = {
            'policy_number': forms.TextInput(attrs={'class': 'form-control'}),
            'policy_type': forms.Select(attrs={'class': 'form-control'}),
            'holder_name': forms.TextInput(attrs={'class': 'form-control'}),
            'holder_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'holder_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'premium_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'sum_insured': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'coverage_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class PremiumCalculationForm(forms.ModelForm):
    class Meta:
        model = PremiumCalculation
        fields = ['base_premium', 'risk_factor', 'tax_rate', 'discount_percentage', 'notes']
        widgets = {
            'base_premium': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'risk_factor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001'}),
            'tax_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'discount_percentage': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
