from django import forms
from .models import Agent, Commission, CommissionPayment

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['agent_code', 'name', 'email', 'phone', 'agent_type', 'commission_rate', 'is_active']
        widgets = {
            'agent_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_type': forms.Select(attrs={'class': 'form-control'}),
            'commission_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['commission_number', 'agent', 'policy', 'commission_rate', 'base_amount', 'commission_date']
        widgets = {
            'commission_number': forms.TextInput(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),
            'policy': forms.Select(attrs={'class': 'form-control'}),
            'commission_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'base_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'commission_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class CommissionPaymentForm(forms.ModelForm):
    class Meta:
        model = CommissionPayment
        fields = ['payment_id', 'amount', 'payment_method', 'payment_date', 'reference_number', 'remarks']
        widgets = {
            'payment_id': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
