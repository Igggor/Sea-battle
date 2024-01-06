from django.db import models
import uuid
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField()
    # games = models.ManyToManyField("Game")
    awards = models.ManyToManyField("Award")


class Award(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# class Game(models.Model):
#     name = models.CharField()
#     description = models.CharField()
#     admin = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     users = models.ManyToManyField("Profile")
