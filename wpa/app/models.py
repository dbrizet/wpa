from __future__ import unicode_literals

from django.db import models

# Team
class Team(models.Model):
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return ''.join([self.name])

# TeamLogo
class TeamLogo(models.Model):
    file = models.FileField(upload_to='team_logos/%Y/%m/%d')
