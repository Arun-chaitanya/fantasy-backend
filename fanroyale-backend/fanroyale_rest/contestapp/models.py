from django.db import models
import uuid
from matchapp.models import Match, Team
from core.models import User


class Contest(models.Model):
    CONTEST_TYPE = (
        ("1", "1"),
        ("2", "2")
    )
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    # contest_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(verbose_name="match created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="match updated at", auto_now=True)
    fees = models.IntegerField()
    flexibility = models.BooleanField(default=True)
    max_spots = models.IntegerField()
    max_winners = models.IntegerField()
    max_decks = models.IntegerField()
    contest_type = models.CharField(max_length=100, choices=CONTEST_TYPE)
    participants = models.ManyToManyField(User, through="ContestParticipants")


class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    points = models.DecimalField(verbose_name="total credits", decimal_places=2, max_digits=6)
    teams = models.ManyToManyField(Team)  # this needs to be changed


class ContestParticipants(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    rank = models.IntegerField()
    prize_money = models.DecimalField(verbose_name="prize money", decimal_places=2, max_digits=6, null=True)


