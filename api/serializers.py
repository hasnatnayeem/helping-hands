from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    donor_name = serializers.ReadOnlyField(source='donor.first_name')
    collector_name = serializers.ReadOnlyField(source='collector.username')

    class Meta:
        model = Donation
        fields = ('id', 'donor_name' ,'amount', 'collector_name', 'collected_at')
