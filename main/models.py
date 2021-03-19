from django.db import models
import re



# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, form_data):
        errors = {}
        EMAIL_REGEX = EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(form_data['first_name']) < 1:
            errors['first_name'] = "Please provide your first name"
        if len(form_data['last_name']) < 1:
            errors['last_name'] = "Please provide your last name"
        if not EMAIL_REGEX.match(form_data['email']):
            errors['email'] = "Email doesn't look right, try again!"
        if len(form_data['phone']) < 10:
            errors['phone'] = "Please provide a real phone number"
        return errors


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    created_month = models.CharField(max_length=3)
    created_year = models.CharField(max_length=4)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubscriberManager(models.Manager):
    def subscriber_validator(self, form_data):
        errors = {}
        EMAIL_REGEX = EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(form_data['first_name']) < 1:
            errors['first_name'] = "Please provide your first name"
        if len(form_data['last_name']) < 1:
            errors['last_name'] = "Please provide your last name"
        if not EMAIL_REGEX.match(form_data['email']):
            errors['email'] = "Email doesn't look right, try again!"
        if len(form_data['phone']) < 10:
            errors['phone'] = "Please provide a real phone number"
        return errors


class Subscriber(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    objects = SubscriberManager()
    active_subscriber = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("created_at", "first_name", "last_name", "email", "phone")
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.email}, {self.phone}, {str(self.created_at)}"


class NewsLetterSubscriberManager(models.Manager):
    def nl_subscriber_validator(self, form_data):
        errors = {}
        EMAIL_REGEX = EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form_data['email']):
            errors['email'] = "Email doesn't look right, try again!"
        return errors

class NewsLetterSubscriber(models.Model):
    email = models.EmailField()
    active_subscriber = models.BooleanField(default=True)
    objects = NewsLetterSubscriberManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClientManager(models.Manager):
    def client_validator(self, form_data):
        errors = {}
        EMAIL_REGEX = EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(form_data['name']) < 4:
            errors['name'] = "Please provide your full name"
        if not EMAIL_REGEX.match(form_data['email']):
            errors['email'] = "Email doesn't look right, try again!"
        if len(form_data['phone']) < 10:
            errors['phone'] = "Please provide a real phone number"
        if len(form_data['message']) < 10:
            errors['message'] = "Please be descriptive so we can no how to help you best!"
        return errors


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()
    objects = ClientManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
