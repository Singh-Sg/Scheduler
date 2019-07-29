from rest_framework.decorators import detail_route
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import firstAsynchronous
from celery import Celery
from celery.schedules import crontab
from scheduler.celery import celery_app
from django_celery_beat.models import PeriodicTasks, CrontabSchedule
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
import datetime

def index(request):
    firstAsynchronous.delay('Las Vegas')
    return HttpResponse("Hello, world. You're at the polls index.")


class CustomAuthToken(ObtainAuthToken):
    """
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        LoginDetials.objects.create(user_id=user)
        firstAsynchronous.delay(10)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

from datetime import timedelta


class WeatherViewSet(APIView):
    """
    """
    def get(self, request):
        PeriodicTask.objects.all().delete()
        IntervalSchedule.objects.all().delete()
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=7,
            period=IntervalSchedule.SECONDS,
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name='This is first PeriodicTask this will run every 3 sec',
            task='apis.tasks.first_periodic_task',
            args=json.dumps(['arg1', 'arg2']),
            # kwargs=json.dumps({
            #     'be_careful': True,
            # }),
            expires=datetime.datetime.now() + timedelta(seconds=50),
        )


        # schedule, _ = CrontabSchedule.objects.get_or_create(
        #     minute='55',
        #     hour='13',
        #     day_of_week='*',
        #     day_of_month='*',
        #     month_of_year='*',
        # )
        # PeriodicTask.objects.create(
        #     crontab=schedule,
        #     name='first crontab',
        #     task='apis.tasks.second_periodic_task',
        # )
        # update periodic tasks in bulk,
        # PeriodicTasks.changed()
        return Response({"success": "success"})
