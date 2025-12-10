from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Agent, Commission, CommissionPayment
from .forms import AgentForm, CommissionForm, CommissionPaymentForm

class AgentListView(LoginRequiredMixin, ListView):
    model = Agent
    template_name = 'commissions/agent_list.html'
    context_object_name = 'agents'
    paginate_by = 20


class AgentDetailView(LoginRequiredMixin, DetailView):
    model = Agent
    template_name = 'commissions/agent_detail.html'
    context_object_name = 'agent'


class AgentCreateView(LoginRequiredMixin, CreateView):
    model = Agent
    form_class = AgentForm
    template_name = 'commissions/agent_form.html'
    success_url = reverse_lazy('commissions:list')


class CommissionListView(LoginRequiredMixin, ListView):
    model = Commission
    template_name = 'commissions/commission_list.html'
    context_object_name = 'commissions'
    paginate_by = 20


class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = 'commissions/commission_detail.html'
    context_object_name = 'commission'


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commission_form.html'
    success_url = reverse_lazy('commissions:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.calculate_commission()
        self.object.save()
        return response


def commission_dashboard(request):
    """Commission dashboard view"""
    agents = Agent.objects.all()
    commissions = Commission.objects.all()
    total_commission = sum(c.commission_amount for c in commissions)
    paid_commission = sum(c.commission_amount for c in commissions.filter(status='PAID'))
    
    context = {
        'agents': agents,
        'commissions': commissions,
        'total_commission': total_commission,
        'paid_commission': paid_commission,
        'pending_commission': total_commission - paid_commission,
    }
    return render(request, 'commissions/commission_dashboard.html', context)
