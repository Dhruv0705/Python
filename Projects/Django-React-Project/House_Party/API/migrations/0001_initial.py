# Generated by Django 4.1.4 on 2023-01-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(default='', max_length=8, unique=True)),
                ('Host', models.CharField(max_length=50, unique=True)),
                ('GuestCanPause', models.BooleanField(default=False)),
                ('VotesToSkip', models.IntegerField(default=1)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
