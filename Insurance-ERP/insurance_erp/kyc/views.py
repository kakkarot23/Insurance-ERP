from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import KYCProfile
from .forms import KYCProfileForm, KYCVerificationForm

class KYCListView(LoginRequiredMixin, ListView):
    model = KYCProfile
    template_name = 'kyc/kyc_list.html'
    context_object_name = 'kyc_profiles'
    paginate_by = 20


class KYCDetailView(LoginRequiredMixin, DetailView):
    model = KYCProfile
    template_name = 'kyc/kyc_detail.html'
    context_object_name = 'kyc_profile'


class KYCCreateView(LoginRequiredMixin, CreateView):
    model = KYCProfile
    form_class = KYCProfileForm
    template_name = 'kyc/kyc_form.html'
    success_url = reverse_lazy('kyc:list')


class KYCVerificationView(LoginRequiredMixin, UpdateView):
    model = KYCProfile
    form_class = KYCVerificationForm
    template_name = 'kyc/kyc_verification.html'
    success_url = reverse_lazy('kyc:list')

    def form_valid(self, form):
        form.instance.verified_by = self.request.user
        return super().form_valid(form)
