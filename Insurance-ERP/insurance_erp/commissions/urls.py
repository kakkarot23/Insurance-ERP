from django.urls import path
from . import views

app_name = 'commissions'

urlpatterns = [
    path('', views.commission_dashboard, name='list'),
    path('agents/', views.AgentListView.as_view(), name='agent_list'),
    path('agents/create/', views.AgentCreateView.as_view(), name='agent_create'),
    path('agents/<int:pk>/', views.AgentDetailView.as_view(), name='agent_detail'),
    path('commissions/', views.CommissionListView.as_view(), name='commission_list'),
    path('commissions/create/', views.CommissionCreateView.as_view(), name='commission_create'),
    path('commissions/<int:pk>/', views.CommissionDetailView.as_view(), name='commission_detail'),
]
