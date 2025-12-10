from django.contrib import admin
from .models import Policy, PremiumCalculation

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'holder_name', 'policy_type', 'status', 'premium_amount', 'created_at')
    list_filter = ('status', 'policy_type', 'created_at')
    search_fields = ('policy_number', 'holder_name', 'holder_email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Policy Information', {
            'fields': ('policy_number', 'policy_type', 'status')
        }),
        ('Holder Details', {
            'fields': ('holder_name', 'holder_email', 'holder_phone')
        }),
        ('Coverage Information', {
            'fields': ('premium_amount', 'sum_insured', 'coverage_details')
        }),
        ('Policy Period', {
            'fields': ('start_date', 'end_date')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PremiumCalculation)
class PremiumCalculationAdmin(admin.ModelAdmin):
    list_display = ('policy', 'base_premium', 'risk_factor', 'total_premium', 'calculated_at')
    list_filter = ('calculated_at',)
    search_fields = ('policy__policy_number',)
    readonly_fields = ('calculated_at', 'total_premium')
