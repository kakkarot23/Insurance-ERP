from django.contrib import admin
from .models import KYCProfile

@admin.register(KYCProfile)
class KYCProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'kyc_type', 'status', 'created_at')
    list_filter = ('status', 'kyc_type', 'created_at')
    search_fields = ('full_name', 'email', 'aadhar_number', 'pan_card')
    readonly_fields = ('id', 'created_at', 'updated_at')
