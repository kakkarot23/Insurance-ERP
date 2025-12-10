from django import forms
from .models import Claim, ClaimDocument

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['claim_number', 'policy', 'claim_date', 'incident_date', 
                  'claim_amount', 'description', 'status']
        widgets = {
            'claim_number': forms.TextInput(attrs={'class': 'form-control'}),
            'policy': forms.Select(attrs={'class': 'form-control'}),
            'claim_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'incident_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'claim_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class ClaimApprovalForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['status', 'approved_amount', 'rejection_reason']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'approved_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'rejection_reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
