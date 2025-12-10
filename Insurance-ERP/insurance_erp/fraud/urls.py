from django.urls import path
from . import views

app_name = 'fraud'

urlpatterns = [
    path('', views.FraudRiskListView.as_view(), name='list'),
    path('create/', views.FraudRiskCreateView.as_view(), name='create'),
    path('<int:pk>/', views.FraudRiskDetailView.as_view(), name='detail'),
    path('<int:pk>/investigate/', views.FraudInvestigationView.as_view(), name='investigate'),
]
