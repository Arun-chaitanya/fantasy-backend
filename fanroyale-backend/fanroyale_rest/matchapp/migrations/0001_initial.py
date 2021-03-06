# Generated by Django 3.2.4 on 2021-06-15 20:02

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('short_name', models.CharField(max_length=15, unique=True)),
                ('type', models.CharField(choices=[('TDM', 'Team Death Match'), ('Battle', 'Battle Royale'), ('Strategy', 'Strategy')], max_length=100)),
                ('device', models.CharField(choices=[('Mobile', 'Mobile'), ('PC', 'PC'), ('Console', 'Console')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('day', models.PositiveIntegerField(blank=True, null=True)),
                ('match_number', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='match created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='match updated at')),
                ('start_datetime', models.DateTimeField(verbose_name='match Start date and time')),
                ('end_datetime', models.DateTimeField(blank=True, null=True, verbose_name='match end date and time')),
                ('status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Live', 'Live'), ('Completed', 'Completed')], max_length=100)),
                ('type', models.CharField(choices=[('MatchWise', 'Match Wise'), ('DayWise', 'Day Wise'), ('TournamentWise', 'Tournament Wise')], max_length=100)),
                ('total_credits', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='total credits')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchapp.game')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('logo_url', models.URLField(verbose_name='team logo url')),
                ('country', models.CharField(max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchapp.game')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='tournament created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='tournament updated at')),
                ('start_datetime', models.DateTimeField(verbose_name='tournament Start date and time')),
                ('end_datetime', models.DateTimeField(verbose_name='tournament end date and time')),
                ('status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Live', 'Live'), ('Completed', 'Completed')], max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchapp.game')),
                ('teams', models.ManyToManyField(to='matchapp.Team')),
            ],
        ),
        migrations.CreateModel(
            name='MatchParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_credits', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='total credits')),
                ('team_rank', models.IntegerField(null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchapp.match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchapp.team')),
            ],
            options={
                'unique_together': {('match', 'team')},
            },
        ),
        migrations.AddField(
            model_name='match',
            name='teams',
            field=models.ManyToManyField(through='matchapp.MatchParticipation', to='matchapp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchapp.tournament'),
        ),
    ]
