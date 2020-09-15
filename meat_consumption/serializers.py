from .models import DailyConsumption, WeeklyConsumption
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class DailyConsumptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = DailyConsumption

        # what are the fields you would like to serialize, i.e. convert back and forth to json data
        # django provides the id, i.e. the primary key
        fields = ('consumed', 'daily_servings', 'day_consumed')


class WeeklyConsumptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WeeklyConsumption
        fields = ('weekly_total_consumption', 'week_start')