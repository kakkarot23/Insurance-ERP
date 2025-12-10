from django.contrib import admin
from .models import Claim, ClaimDocument

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('claim_number', 'policy', 'claim_date', 'status', 'claim_amount', 'approved_amount')
    list_filter = ('status', 'claim_date')
    search_fields = ('claim_number', 'policy__policy_number')


@admin.register(ClaimDocument)
class ClaimDocumentAdmin(admin.ModelAdmin):
    list_display = ('claim', 'document_type', 'uploaded_at')
    search_fields = ('claim__claim_number',)
