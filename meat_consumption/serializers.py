from .models import DailyConsumption, WeeklyConsumption
from rest_framework import serializers


class DailyConsumptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    weekly_total = serializers.ReadOnlyField(source='weekly_consumption.weekly_total')

    class Meta:
        model = DailyConsumption
        fields = ('id', 'weekly_consumption_id', 'owner', 'consumed', 'daily_servings', 'day_consumed', 'weekly_total')


class WeeklyConsumptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WeeklyConsumption
        fields = ('week_number', 'owner', 'id')