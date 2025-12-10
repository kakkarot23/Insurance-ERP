from django.contrib import admin
from .models import Agent, Commission, CommissionPayment

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('agent_code', 'name', 'agent_type', 'commission_rate', 'is_active')
    list_filter = ('agent_type', 'is_active')
    search_fields = ('agent_code', 'name', 'email')


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ('commission_number', 'agent', 'policy', 'commission_amount', 'status', 'commission_date')
    list_filter = ('status', 'commission_date')
    search_fields = ('commission_number', 'agent__name', 'policy__policy_number')


@admin.register(CommissionPayment)
class CommissionPaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'commission', 'amount', 'payment_method', 'payment_date')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('payment_id', 'commission__commission_number', 'reference_number')
