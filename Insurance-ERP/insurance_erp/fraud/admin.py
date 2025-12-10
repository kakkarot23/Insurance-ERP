from django.contrib import admin
from .models import FraudRisk

@admin.register(FraudRisk)
class FraudRiskAdmin(admin.ModelAdmin):
    list_display = ('policy', 'risk_level', 'risk_score', 'status', 'created_at')
    list_filter = ('risk_level', 'status', 'created_at')
    search_fields = ('policy__policy_number', 'description')
    readonly_fields = ('risk_score', 'created_at', 'updated_at')
