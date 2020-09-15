from .models import WeeklyConsumption, DailyConsumption
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DailyConsumptionSerializer, WeeklyConsumptionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class DailyConsumptionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DailyConsumptionSerializer

    #############################################################################
    # READ - SHOW ALL DAYS (just for testing)
    def get_queryset(self):
        queryset = DailyConsumption.objects.all().filter(owner=self.request.user)
        return queryset

    #############################################################################
    # READ - SHOW JUST ONE DAY
    def retrieve(self, request, *args, **kwargs):
        queryset = DailyConsumption.objects.filter(pk=self.kwargs.get('daily_consumption_pk'))
        return queryset

    #############################################################################
    # CREATE - CREATE A RECORD OF A DAY THAT MEAT WAS CONSUMED
    def create(self, request, *args, **kwargs):
        # check if the day already exists for the current logged in user
        day = DailyConsumption.objects.filter(
            owner=request.user,
            consumed=request.data.get('consumed'),
            daily_servings=request.data.get('daily_servings'),
            day_consumed=request.data.get('day_consumed')
        )
        if day:
            msg = 'Log for this day already exists'
            raise ValidationError(msg)
        return super().create(request)

    # saves the information
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    #############################################################################
    # DESTROY - DELETE A DAILY RECORD OF WHEN MEAT WAS CONSUMED
    # look into only deleting ALL records for a user if they just want to restart the week
    def destroy(self, request, *args, **kwargs):

        # gets the primary key of the day if it exists
        daily_consumption = DailyConsumption.objects.get(pk=self.kwargs["daily_consumption_pk"])

        # finds if the logged in user is the owner of the category
        if not request.user == daily_consumption.owner:
            raise PermissionDenied("You cannot delete this record")
        return super().destroy(request, *args, **kwargs)

    #############################################################################
    # UPDATE - PARTIAL UPDATE FOR JUST SERVING WHEN DAILY RECORD HAS BEEN CREATED
    # Don't allow user to input new date if already entered. Only allow user to update consumed and servings
