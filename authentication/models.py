#DJANGO
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(
        'Email address',
        unique=True,
        error_messages={
            'unique': 'Email already registered'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)