from django.db import models
import uuid


class Game(models.Model):
    CATEGORY = (
        ("TDM", "Team Death Match"),
        ("Battle", "Battle Royale"),
        ("Strategy", "Strategy")
    )

    DEVICE = (
        ("Mobile", "Mobile"),
        ("PC", "PC"),
        ("Console", "Console")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=15, unique=True)
    type = models.CharField(max_length=100, choices=CATEGORY)
    device = models.CharField(max_length=100, choices=DEVICE)

    def __str__(self):
        return self.name


class Team(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    logo_url = models.URLField(verbose_name="team logo url")
    country = models.CharField(max_length=100)


class Tournament(models.Model):
    STATUS = (
        ("Upcoming", "Upcoming"),
        ("Live", "Live"),
        ("Completed", "Completed")
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(verbose_name="tournament created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="tournament updated at", auto_now=True)
    start_datetime = models.DateTimeField(verbose_name="tournament Start date and time")
    end_datetime = models.DateTimeField(verbose_name="tournament end date and time")
    status = models.CharField(max_length=100, choices=STATUS)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name


class MatchManager(models.Manager):
    def get_matches_by_game(self, game_name):
        matches_list = self.filter(game__name__exact=game_name, status__exact="Upcoming")
        match_wise = []
        day_wise = []
        tournament_wise = []
        for x in matches_list:
            if x.type == "MatchWise":
                match_wise.append(x)
            elif x.type == "DayWise":
                day_wise.append(x)
            elif x.type == "TournamentWise":
                tournament_wise.append(x)
        return {"match_wise": match_wise, "day_wise": day_wise, "tournament_wise": tournament_wise}


class Match(models.Model):
    STATUS = (
        ("Upcoming", "Upcoming"),
        ("Live", "Live"),
        ("Completed", "Completed")
    )

    MATCH_TYPE = (
        ("MatchWise", "Match Wise"),
        ("DayWise", "Day Wise"),
        ("TournamentWise", "Tournament Wise")
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day = models.PositiveIntegerField(null=True, blank=True)
    match_number = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="match created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="match updated at", auto_now=True)
    start_datetime = models.DateTimeField(verbose_name="match Start date and time")
    end_datetime = models.DateTimeField(verbose_name="match end date and time", null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS)
    type = models.CharField(max_length=100, choices=MATCH_TYPE)
    total_credits = models.DecimalField(verbose_name="total credits", decimal_places=1, max_digits=4)
    teams = models.ManyToManyField(Team, through='MatchParticipation')

    objects = MatchManager()

    def __str__(self):
        return self.game.name + self.type


class MatchParticipation(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_credits = models.DecimalField(verbose_name="total credits", decimal_places=1, max_digits=3)
    team_rank = models.IntegerField(null=True)

    class Meta:
        unique_together = [['match', 'team']]

