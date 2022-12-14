# Generated by Django 4.1 on 2022-08-29 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=200)),
                ('room_Name', models.CharField(max_length=200)),
                ('joinedAt', models.TimeField(auto_now_add=True)),
                ('cameraOn', models.BooleanField(default=True)),
                ('micOn', models.BooleanField(default=True)),
                ('screenOn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videocall.participant')),
            ],
        ),
    ]
