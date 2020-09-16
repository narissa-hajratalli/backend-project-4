from .models import DailyConsumption, WeeklyConsumption
from rest_framework import serializers


class DailyConsumptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    weekly_total = serializers.ReadOnlyField(source='weekly_consumption.weekly_total')

    class Meta:
        model = DailyConsumption

        # what are the fields you would like to serialize, i.e. convert back and forth to json data
        # django provides the id, i.e. the primary key
        fields = ('consumed', 'daily_servings', 'day_consumed', 'owner', 'id', 'weekly_total')


class WeeklyConsumptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WeeklyConsumption
        # fields = ('weekly_total_consumption', 'week_start')