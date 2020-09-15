from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from meat_consumption.views import DailyConsumptionViewSet

router = routers.DefaultRouter()
# base endpoint, ...meat_consumption/daily_consumption/
router.register('daily_consumption', DailyConsumptionViewSet, basename='daily_consumption')


custom_urlpatterns = [
   url(r'daily_consumption/(?P<daily_consumption_pk>\d+)$', DailyConsumptionViewSet, name='daily_consumption_per_day')
   # Example pattern is: localhost:8000/meat_consumption/daily_consumption/1
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns