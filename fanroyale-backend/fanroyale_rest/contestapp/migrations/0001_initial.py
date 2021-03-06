# Generated by Django 3.2.8 on 2021-10-10 06:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('matchapp', '0003_alter_match_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='match created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='match updated at')),
                ('fees', models.IntegerField()),
                ('flexibility', models.BooleanField(default=True)),
                ('max_spots', models.IntegerField()),
                ('max_winners', models.IntegerField()),
                ('max_decks', models.IntegerField()),
                ('contest_type', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=100)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchapp.match')),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('points', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='total credits')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchapp.match')),
                ('teams', models.ManyToManyField(to='matchapp.Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='ContestParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('prize_money', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='prize money')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contestapp.contest')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contestapp.deck')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='participants',
            field=models.ManyToManyField(through='contestapp.ContestParticipants', to='core.User'),
        ),
    ]
