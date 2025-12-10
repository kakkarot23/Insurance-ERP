from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib import messages

@require_http_methods(["GET", "POST"])
def user_login(request):
    """Custom login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html', {'title': 'Insurance ERP Login'})

def user_logout(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    """Main dashboard view"""
    context = {
        'title': 'Insurance ERP Dashboard',
        'modules': [
            {'name': 'Policy Lifecycle', 'url': 'policies:list', 'icon': 'document'},
            {'name': 'Premium Calculations', 'url': 'policies:premium', 'icon': 'calculator'},
            {'name': 'KYC Onboarding', 'url': 'kyc:list', 'icon': 'user'},
            {'name': 'Claims Processing', 'url': 'claims:list', 'icon': 'clipboard'},
            {'name': 'Fraud Detection', 'url': 'fraud:list', 'icon': 'shield'},
            {'name': 'Commission Module', 'url': 'commissions:list', 'icon': 'money'},
        ]
    }
    return render(request, 'dashboard.html', context)
