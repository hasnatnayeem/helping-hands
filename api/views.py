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
from .serializers import ProfileSerializer
from datetime import datetime
from django.db.models import *
from rest_framework.decorators import api_view
from django.core import serializers
from django.db import connection


class LoginView(TokenObtainSlidingView):
    def post(self, request, *args, **kwargs):
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
                                'name': profile.name,
                                'address': profile.address,
                                'phone': profile.phone,
                        },
                        'token': str(token),
                }, status=status.HTTP_200_OK)



class DonationView(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    http_method_names = ['get','post']

    def get_queryset(self):
        today = datetime.now()
        queryset = Donation.objects.all().order_by('-collected_at').filter(collected_at__year=today.year, collected_at__month=today.month)
        collector_id = self.request.query_params.get('collector_id', None)
        if collector_id is not None:
            queryset = queryset.filter(collector_id=collector_id)
        return queryset


@api_view()
def get_donation_summary(request):
    today = datetime.now()
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATE_FORMAT(collected_at, '%M %Y') as d, sum(amount) FROM api_donation WHERE DATE_FORMAT(collected_at, '%Y-%m') >= '{}' GROUP BY d".format(datetime.strftime(today,'%Y-%m')))
        summary = cursor.fetchall()
    
    queryset = Donation.objects.all().order_by('-collected_at').filter(collected_at__year=today.year, collected_at__month=today.month)
    collector_id = request.query_params.get('collector_id', None)
    if collector_id is not None:
        queryset = queryset.filter(collector_id=collector_id)

    donations = DonationSerializer(queryset, many=True).data

    return Response({
                    'donations': donations,
                    'summary': summary,
            }, status=status.HTTP_200_OK)
    

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get']