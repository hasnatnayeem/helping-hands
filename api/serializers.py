from rest_framework import serializers
from .models import Donation
from .models import Expense
from .models import Profile

class DonationSerializer(serializers.ModelSerializer):
    donor_name = serializers.ReadOnlyField(source='donor.name')
    photo = serializers.ReadOnlyField(source='donor.photo')
    collector_name = serializers.ReadOnlyField(source='collector.username')

    class Meta:
        model = Donation
        fields = ('id', 'donor', 'donor_name', 'photo' ,'amount', 'collector', 'collector_name', 'collected_at')
        
    def to_representation(self, instance):
        representation = super(DonationSerializer, self).to_representation(instance)
        representation['collected_at'] = instance.collected_at.strftime('%d-%m-%Y')
        return representation


class ExpenseSerializer(serializers.ModelSerializer):
    spender_name = serializers.ReadOnlyField(source='spender.name')
    photo = serializers.ReadOnlyField(source='spender.photo')

    class Meta:
        model = Expense
        fields = ('id', 'spender', 'spender_name', 'photo' ,'amount', 'reference', 'spent_at')
        
    def to_representation(self, instance):
        representation = super(ExpenseSerializer, self).to_representation(instance)
        representation['spent_at'] = instance.spent_at.strftime('%d-%m-%Y')
        return representation



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'photo', 'phone', 'email', 'blood_group')
        