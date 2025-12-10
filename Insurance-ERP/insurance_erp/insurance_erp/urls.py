"""
URL configuration for insurance_erp project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('api-auth/', include('rest_framework.urls')),
    path('policies/', include('policies.urls')),
    path('claims/', include('claims.urls')),
    path('kyc/', include('kyc.urls')),
    path('fraud/', include('fraud.urls')),
    path('commissions/', include('commissions.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
