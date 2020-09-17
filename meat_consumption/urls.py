from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from meat_consumption.views import DailyConsumptionViewSet, WeeklyConsumptionViewSet, WeeklyDaily

router = routers.DefaultRouter()
# base endpoint, ...meat_consumption/daily_consumption/
router.register('daily_consumption', DailyConsumptionViewSet, basename='daily_consumption')
router.register('weekly_consumption', WeeklyConsumptionViewSet, basename='weekly_consumption')


custom_urlpatterns = [
   # url(r'daily_consumption/(?P<pk>\d+)$', DailyConsumptionViewSet, name='daily_consumption'),
   # url(r'weekly_consumption/(?P<pk>\d+)$', WeeklyConsumptionViewSet.destroy, name='weekly_consumption'),
   url(r'weekly_consumption/(?P<weekly_consumption_pk>\d+)/daily_consumption$', WeeklyDaily.as_view(), name='weekly_daily')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns