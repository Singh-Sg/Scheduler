import requests
from celery import Celery
from celery import shared_task
from celery.schedules import crontab
from scheduler.celery import celery_app
from django_celery_beat.models import PeriodicTask, PeriodicTasks

app = Celery()


@shared_task
def firstAsynchronous(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9f7a614906fece261ec9126777520753'
    city_weather = requests.get(url.format(city)).json()
    print(city_weather)


@celery_app.on_after_finalize.connect
def first_periodic_tasks(sender, **kwargs):
    city = 'Delhi'
    # Executes every day 3 PM
    sender.add_periodic_task(
        crontab(minute=0, hour=15),
        threePmDaily.s(city),
    )


@celery_app.task
def threePmDaily(arg):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9f7a614906fece261ec9126777520753'
    city_weather = requests.get(url.format(arg)).json()
    print(city_weather)


@celery_app.task
def first_periodic_task(name, args, expires):
    print("hello i'm running every 3 second")
    


@celery_app.task(bind=True)
def second_periodic_task(arg):
    print("hello i'm running next one min")
