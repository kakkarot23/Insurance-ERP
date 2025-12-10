from django.urls import path
from . import views

app_name = 'kyc'

urlpatterns = [
    path('', views.KYCListView.as_view(), name='list'),
    path('create/', views.KYCCreateView.as_view(), name='create'),
    path('<uuid:pk>/', views.KYCDetailView.as_view(), name='detail'),
    path('<uuid:pk>/verify/', views.KYCVerificationView.as_view(), name='verify'),
]
