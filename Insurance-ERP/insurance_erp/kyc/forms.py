from django import forms
from .models import KYCProfile

class KYCProfileForm(forms.ModelForm):
    class Meta:
        model = KYCProfile
        fields = [
            'full_name', 'email', 'phone', 'kyc_type',
            'identity_document_type', 'identity_document_number', 'identity_document_file',
            'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country',
            'address_proof_file', 'pan_card', 'aadhar_number'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'kyc_type': forms.Select(attrs={'class': 'form-control'}),
            'identity_document_type': forms.TextInput(attrs={'class': 'form-control'}),
            'identity_document_number': forms.TextInput(attrs={'class': 'form-control'}),
            'identity_document_file': forms.FileInput(attrs={'class': 'form-control'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'address_proof_file': forms.FileInput(attrs={'class': 'form-control'}),
            'pan_card': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class KYCVerificationForm(forms.ModelForm):
    class Meta:
        model = KYCProfile
        fields = ['status', 'verification_notes']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'verification_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
