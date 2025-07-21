from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add future fields here like preferred_currency, timezone, etc.
    pass
