from django.contrib import admin
from .models import Subscriber, NewsLetterSubscriber, Blog, Client

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'author', 'category', 'created_at', 'updated_at']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "active_subscriber")


@admin.register(NewsLetterSubscriber)
class NLSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "active_subscriber", "created_at")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message")