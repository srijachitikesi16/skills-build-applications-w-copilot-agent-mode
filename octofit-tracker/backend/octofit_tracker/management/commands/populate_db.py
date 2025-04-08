from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='john.doe@example.com', name='John Doe', age=25),
            User(email='jane.smith@example.com', name='Jane Smith', age=30),
            User(email='alice.wonderland@example.com', name='Alice Wonderland', age=22),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com']),
            Team(name='Team Beta', members=['alice.wonderland@example.com']),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user='john.doe@example.com', activity_type='Running', duration=30, date=date(2025, 4, 8)),
            Activity(user='jane.smith@example.com', activity_type='Cycling', duration=60, date=date(2025, 4, 7)),
            Activity(user='alice.wonderland@example.com', activity_type='Swimming', duration=45, date=date(2025, 4, 6)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team='Team Alpha', points=150),
            Leaderboard(team='Team Beta', points=100),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Morning Run', description='A 5km run to start the day'),
            Workout(name='Cycling Session', description='An hour of cycling at moderate intensity'),
            Workout(name='Swimming Laps', description='45 minutes of swimming laps'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
