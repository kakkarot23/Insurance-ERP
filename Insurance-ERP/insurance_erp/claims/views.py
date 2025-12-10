from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Claim
from .forms import ClaimForm, ClaimApprovalForm

class ClaimListView(LoginRequiredMixin, ListView):
    model = Claim
    template_name = 'claims/claim_list.html'
    context_object_name = 'claims'
    paginate_by = 20


class ClaimDetailView(LoginRequiredMixin, DetailView):
    model = Claim
    template_name = 'claims/claim_detail.html'
    context_object_name = 'claim'


class ClaimCreateView(LoginRequiredMixin, CreateView):
    model = Claim
    form_class = ClaimForm
    template_name = 'claims/claim_form.html'
    success_url = reverse_lazy('claims:list')


class ClaimApprovalView(LoginRequiredMixin, UpdateView):
    model = Claim
    form_class = ClaimApprovalForm
    template_name = 'claims/claim_approval.html'
    success_url = reverse_lazy('claims:list')
