from django.test import TestCase

from app.models import Team

class TeamTests(TestCase):
    """Team model tests."""
    def test_str(self):
        team = Team(name='team1')
        self.assertEquals(str(team),'team1')
