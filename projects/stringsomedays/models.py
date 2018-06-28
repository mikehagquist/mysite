import datetime

from django.db import models
from django.utils import timezone


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')

    def __str__(self):
        return self.team_name
        
    def was_created_recently(self):
        return self.create_date >= timezone.now() - datetime.timedelta(days=1)

class TeamMembers(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_member = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.team_member
