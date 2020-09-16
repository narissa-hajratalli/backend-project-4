from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from meat_consumption.views import DailyConsumptionViewSet, WeeklyConsumptionTotal

router = routers.DefaultRouter()
# base endpoint, ...meat_consumption/daily_consumption/
router.register('daily_consumption', DailyConsumptionViewSet, basename='daily_consumption')


custom_urlpatterns = [
   url(r'daily_consumption/(?P<pk>\d+)$', DailyConsumptionViewSet.retrieve, name='daily_consumption_per_day'),
   url(r'daily_consumption/weekly_total/$', WeeklyConsumptionTotal, name='weekly_total')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns