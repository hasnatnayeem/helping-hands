from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginView
from django.contrib.auth.models import User

router = routers.DefaultRouter()
# router.register('donations', views.DonationView, 'Donation')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('login/', LoginView.as_view()),
]
