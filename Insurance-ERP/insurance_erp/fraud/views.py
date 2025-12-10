from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import FraudRisk
from .forms import FraudRiskForm, FraudInvestigationForm

class FraudRiskListView(LoginRequiredMixin, ListView):
    model = FraudRisk
    template_name = 'fraud/fraud_list.html'
    context_object_name = 'fraud_risks'
    paginate_by = 20

    def get_queryset(self):
        return FraudRisk.objects.all().order_by('-risk_score')


class FraudRiskDetailView(LoginRequiredMixin, DetailView):
    model = FraudRisk
    template_name = 'fraud/fraud_detail.html'
    context_object_name = 'fraud_risk'


class FraudRiskCreateView(LoginRequiredMixin, CreateView):
    model = FraudRisk
    form_class = FraudRiskForm
    template_name = 'fraud/fraud_form.html'
    success_url = reverse_lazy('fraud:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.calculate_risk_score()
        self.object.save()
        return response


class FraudInvestigationView(LoginRequiredMixin, UpdateView):
    model = FraudRisk
    form_class = FraudInvestigationForm
    template_name = 'fraud/fraud_investigation.html'
    success_url = reverse_lazy('fraud:list')

    def form_valid(self, form):
        form.instance.assigned_to = self.request.user
        return super().form_valid(form)
