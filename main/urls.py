from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('news', views.news),
    path('news-post', views.newsPost),
    path('subscriber', views.subscriber),
    path('news-subscriber', views.newsSubscriber),
    path('news-subscriber-hp', views.newsSubscriberHP),
    path('contact', views.contact),
    path('contact-us', views.contactUs),
    path('at-home-training', views.atHomeTraining),
    path('fullworkouts', views.fullworkouts),
    path('workout/1&2', views.workoutWeekOne),
    path('workout/3', views.workoutWeekThree),
    path('workout/4', views.workoutWeekFour),
    path('workout/5', views.workoutWeekFive),
    path('workout/6', views.workoutWeekSix),
    path('schedule', views.schedule),
    path('programs', views.programs)
]
