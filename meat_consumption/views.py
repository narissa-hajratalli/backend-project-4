from django.db.models import Sum

from .models import WeeklyConsumption, DailyConsumption
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


################ VIEWS #################
class WeeklyConsumptionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = WeeklyConsumptionSerializer

    #############################################################################
    ##### GET ALL THE WEEKS ####
    def get_queryset(self):
        queryset = WeeklyConsumption.objects.all().filter(owner=self.request.user)
        return queryset

    #############################################################################
    ### GET ONE WEEK ###
    def retrieve(self, request, *args, **kwargs):
        print('*** retrieve is called ***')

        weekly_consumption_instance = self.get_object()

        serializer = WeeklyConsumptionSerializer(weekly_consumption_instance)

        return Response(serializer.data)

    #############################################################################
    #### CREATE A WEEK ###

    def create(self, request, *args, **kwargs):
        weekly_consumption = WeeklyConsumption.objects.filter(
            week_number=request.data.get('week_number'),
            owner=request.user
        )
        if weekly_consumption:
            msg = 'Week number already exists'
            raise ValidationError(msg)
        return super().create(request)

    # saves the information
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    #############################################################################
    ### DELETE A WEEK ###
    # def destroy(self, request, *args, **kwargs):
    #     weekly_consumption = WeeklyConsumption.objects.get(pk=self.kwargs["pk"])
    #
    #     # finds if the logged in user is the owner of the week
    #     if not request.user == weekly_consumption.owner:
    #         raise PermissionDenied("You cannot delete this category")
    #     return super().destroy(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        weekly_consumption = WeeklyConsumption.objects.get(pk=self.kwargs["pk"])
        print(weekly_consumption)

        if not request.user == weekly_consumption.owner:
           raise PermissionDenied("You cannot delete this category")

        return super().destroy(request, *args, **kwargs)

###############################################################################

class WeeklyDaily(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DailyConsumptionSerializer

    def get_queryset(self):
        if self.kwargs.get("weekly_consumption_pk"):
            weekly_consumption = WeeklyConsumption.objects.get(pk=self.kwargs['weekly_consumption_pk'])

            queryset = DailyConsumption.objects.filter(
                owner=self.request.user,
                weekly_consumption=weekly_consumption
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

###############################################################################

class DailyConsumptionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DailyConsumptionSerializer

    #############################################################################
    # READ - SHOW ALL DAYS (regardless of week) (just for testing)
    def get_queryset(self):
        queryset = DailyConsumption.objects.all().filter(owner=self.request.user)
        return queryset

    #############################################################################
    # SHOW ONE - SHOW JUST ONE DAY
    # Ex: /daily_consumption/1
    def retrieve(self, *args, **kwargs):
        queryset = DailyConsumption.objects.get(pk=int(kwargs['pk'][0]))
        results = DailyConsumptionSerializer(queryset)
        return Response(results.data, status=200)

    #############################################################################
    # CREATE - CREATE A RECORD OF A DAY THAT MEAT WAS CONSUMED
    def create(self, request, *args, **kwargs):
        day = DailyConsumption.objects.filter(
            owner=request.user,
            consumed=request.data.get('consumed'),
            daily_servings=request.data.get('daily_servings'),
            day_consumed=request.data.get('day_consumed'),
        )
        if day:
            msg = 'Log for this day already exists'
            raise ValidationError(msg)
        return super().create(request)

    # saves the information
    def perform_create(self, serializer):
        print("perform_create")
        week = WeeklyConsumption.objects.get(pk=self.request.data.get('weekly_consumption_id'))
        serializer.save(owner=self.request.user, weekly_consumption=week)

    #############################################################################
    # DESTROY - DELETE A DAILY RECORD OF WHEN MEAT WAS CONSUMED
    # look into only deleting ALL records for a user if they just want to restart the week
    def destroy(self, request, *args, **kwargs):

        # gets the primary key of the day if it exists
        daily_consumption = DailyConsumption.objects.get(pk=self.kwargs["pk"])

        # finds if the logged in user is the owner of the category
        if not request.user == daily_consumption.owner:
            raise PermissionDenied("You cannot delete this record")
        return super().destroy(request, *args, **kwargs)

    #############################################################################
    # UPDATE - PARTIAL UPDATE FOR JUST SERVING WHEN DAILY RECORD HAS BEEN CREATED
    # Don't allow user to input new date if already entered. Only allow user to update servings.
    # The user will have to delete the entry if they put in an incorrect value for consumed or
    # day_consumed

    def partial_update(self, request, *args, **kwargs):
        daily_consumption_instance = self.get_object()

        daily_consumption_instance.daily_servings = request.data.get('daily_servings',
                                                                     daily_consumption_instance.daily_servings)
        daily_consumption_instance.save()

        serializer = DailyConsumptionSerializer(daily_consumption_instance)
        return Response(serializer.data)

