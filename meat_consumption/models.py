from django.db import models
from django.contrib.auth.models import User, Group
# from p4backend import settings


# Create your models here.


class DailyConsumption(models.Model):
    consumed = models.BooleanField
    daily_servings = models.PositiveSmallIntegerField(0)
    day_consumed = models.DateField  # just the day of the week & date of the day meat was consumed, shows just individual day consumed
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # one user has many daily consumptions

    class Meta:
        verbose_name_plural = 'daily_consumptions'

        def __str__(self):
            return self.servings


class WeeklyConsumption(models.Model):
    # days_consumed_this_week = models.ForeignKey(DailyConsumption, on_delete=models.CASCADE)  # want to capture an array of all days of the week meat was consumed
    weekly_total_consumption = models.ForeignKey(DailyConsumption, on_delete=models.CASCADE)  # use aggregate method to sum the total of servings from DailyConsumption.daily_serving
    week_start = models.DateField # starting day of the week

    class Meta:
        verbose_name_plural = 'weekly_consumptions'

        def __str__(self):
            return self.weekly_total_consumption


