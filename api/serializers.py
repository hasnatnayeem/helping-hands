from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    donor_name = serializers.ReadOnlyField(source='donor.first_name')
    collector_name = serializers.ReadOnlyField(source='collector.username')

    class Meta:
        model = Donation
        fields = ('id', 'donor_name' ,'amount', 'collector_name', 'collected_at')

    def to_representation(self, instance):
        representation = super(DonationSerializer, self).to_representation(instance)
        representation['collected_at'] = instance.collected_at.strftime('%d-%m-%Y')
        return representation
