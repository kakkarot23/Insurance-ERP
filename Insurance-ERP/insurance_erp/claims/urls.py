from django.urls import path
from . import views

app_name = 'claims'

urlpatterns = [
    path('', views.ClaimListView.as_view(), name='list'),
    path('create/', views.ClaimCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ClaimDetailView.as_view(), name='detail'),
    path('<int:pk>/approve/', views.ClaimApprovalView.as_view(), name='approve'),
]
