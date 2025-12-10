from django.urls import path
from . import views

app_name = 'policies'

urlpatterns = [
    path('', views.PolicyListView.as_view(), name='list'),
    path('create/', views.PolicyCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PolicyDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.PolicyUpdateView.as_view(), name='update'),
    path('premium/', views.premium_calculation_view, name='premium'),
]
