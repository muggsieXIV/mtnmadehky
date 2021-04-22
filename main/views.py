from django.shortcuts import render, redirect
from .models import Subscriber, NewsLetterSubscriber, Client
from django.contrib import messages
from datetime import datetime


# views
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')

def newsPost(request):
    return render(request, 'news-single.html')

def atHomeTraining(request):
    return render(request, 'at-home-training.html')


def fullworkouts(request):
    return render(request, 'full-workouts.html')


def workoutWeekOne(request):
    return render(request, 'workout-week-one.html')


def workoutWeekThree(request):
    return render(request, 'workout-week-three.html')


def workoutWeekFour(request):
    return render(request, 'workout-week-four.html')


def workoutWeekFive(request):
    return render(request, 'workout-week-five.html')


def workoutWeekSix(request):
    return render(request, 'workout-week-six.html')


def schedule(request):
    return render(request, 'schedule.html')


def programs(request):
    return render(request, 'programs.html')

# functions
def contactUs(request):
    errors = Client.objects.client_validator(request.POST)
    if len(errors) > 0:
        for message in errors.values():
            messages.error(request, message)
        return redirect("/contact")
    Client.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        phone=request.POST['phone'],
        message=request.POST['message']
    )
    return redirect('/contact')

def subscriber(request):
    errors = Subscriber.objects.subscriber_validator(request.POST)
    if len(errors) > 0:
        for message in errors.values():
            messages.error(request, message)
        return redirect("/")
    Subscriber.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        phone=request.POST['phone'],
    )
    return redirect('/')


def newsSubscriber(request):
    errors = NewsLetterSubscriber.objects.nl_subscriber_validator(request.POST)
    if len(errors) > 0:
        for message in errors.values():
            messages.error(request, message)
        return redirect("/news")
    NewsLetterSubscriber.objects.create(
        email=request.POST['email'],
    )
    return redirect('/news')


def newsSubscriberHP(request):
    errors = NewsLetterSubscriber.objects.nl_subscriber_validator(request.POST)
    if len(errors) > 0:
        for message in errors.values():
            messages.error(request, message)
        return redirect("/")
    NewsLetterSubscriber.objects.create(
        email=request.POST['email'],
    )
    return redirect('/')




