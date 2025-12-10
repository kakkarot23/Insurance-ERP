from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Policy, PremiumCalculation
from .forms import PolicyForm, PremiumCalculationForm

class PolicyListView(LoginRequiredMixin, ListView):
    model = Policy
    template_name = 'policies/policy_list.html'
    context_object_name = 'policies'
    paginate_by = 20

    def get_queryset(self):
        return Policy.objects.all().order_by('-created_at')


class PolicyDetailView(LoginRequiredMixin, DetailView):
    model = Policy
    template_name = 'policies/policy_detail.html'
    context_object_name = 'policy'


class PolicyCreateView(LoginRequiredMixin, CreateView):
    model = Policy
    form_class = PolicyForm
    template_name = 'policies/policy_form.html'
    success_url = reverse_lazy('policies:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PolicyUpdateView(LoginRequiredMixin, UpdateView):
    model = Policy
    form_class = PolicyForm
    template_name = 'policies/policy_form.html'
    success_url = reverse_lazy('policies:list')


def premium_calculation_view(request):
    """Premium calculation view"""
    policies = Policy.objects.all()
    calculations = PremiumCalculation.objects.all()
    
    if request.method == 'POST':
        policy_id = request.POST.get('policy_id')
        try:
            policy = Policy.objects.get(id=policy_id)
            calc, created = PremiumCalculation.objects.get_or_create(policy=policy)
            
            form = PremiumCalculationForm(request.POST, instance=calc)
            if form.is_valid():
                calc = form.save(commit=False)
                calc.calculate_total()
                calc.save()
                policy.premium_amount = calc.total_premium
                policy.save()
                return render(request, 'policies/premium_calculation.html', {
                    'policies': policies,
                    'calculations': calculations,
                    'success': True,
                    'calc': calc
                })
        except Policy.DoesNotExist:
            pass
    
    context = {
        'policies': policies,
        'calculations': calculations,
        'form': PremiumCalculationForm(),
    }
    return render(request, 'policies/premium_calculation.html', context)
