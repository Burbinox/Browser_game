from django.db import models
from django.contrib.auth.models import User


class Stats(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    endurance = models.IntegerField(null=False)
    resistance = models.IntegerField(null=False)
    strength = models.IntegerField(null=False)
    speed = models.IntegerField(null=False)
    agility = models.IntegerField(null=False)
    mind_power = models.IntegerField(null=False)
