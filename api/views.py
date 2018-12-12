from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainSlidingView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile
from .models import Donation
from .serializers import DonationSerializer

class LoginView(TokenObtainSlidingView):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        res = response.data
        req = request.data
        username = req.get('username')
        password = req.get('password')

        if username is None or password is None:
            return Response({'success': False, 
                            'message': 'Missing or incorrect credentials',
                            'data': req},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except:
            return Response({'success': False, 
                            'message': 'User not found'
                            },
                            status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'success': False, 
                            'message': 'Incorrect password',
                            'data': req},
                            status=status.HTTP_403_FORBIDDEN)

        # make token from user found by username
        token = TokenObtainPairSerializer.get_token(user).access_token
        profile = Profile.objects.get(user=user.pk)
        return Response({
                        'user': {
                                'id': user.pk,
                                'profile_id': profile.id,
                                'first_name': profile.first_name,
                                'last_name': profile.last_name,
                                'address': profile.address,
                                'phone': profile.phone,
                        },
                        'token': str(token),
                }, status=status.HTTP_200_OK)



class DonationView(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    http_method_names = ['get','post']

    def get_queryset(self):
        return Donation.objects.all().order_by('-collected_at')
    