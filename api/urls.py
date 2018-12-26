from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginView
from .views import DonationView
from .views import ProfileView
from .views import get_donation_summary

router = routers.DefaultRouter()
router.register('donations', DonationView, 'Donation')
router.register('profiles', ProfileView, 'Profile')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('login/', LoginView.as_view()),
    path('donation-summary/', get_donation_summary)
]
