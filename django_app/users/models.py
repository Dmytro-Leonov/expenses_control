from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    daily_limit = models.FloatField(
        default=settings.DEFAULT_DAILY_LIMIT,
        validators=[MinValueValidator(0, "Daily limit must be positive")],
    )

    def __str__(self):
        return self.email
