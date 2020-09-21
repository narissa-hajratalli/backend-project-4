from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings



# Create your models here.

class WeeklyConsumption(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    week_number = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'weekly_consumptions'

    def consumption_sum(self):
        days = self.dailyconsumption_set.all()
        counter = 0
        for day in days:
            counter += day.daily_servings
        return counter

    weekly_total = property(fget=consumption_sum)

    def __str__(self):
        return self.week_number


class DailyConsumption(models.Model):
    consumed = models.CharField(max_length=3)
    daily_servings = models.PositiveSmallIntegerField(0)
    day_consumed = models.CharField(max_length=50)  # just the day of the week & date of the day meat was consumed, shows just individual day consumed
    weekly_consumption = models.ForeignKey(WeeklyConsumption, on_delete=models.CASCADE, default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'daily_consumptions'

    def __str__(self):
        return self.daily_servings





