# Generated by Django 4.1 on 2022-09-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videocall', '0002_participant_isadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isAdmin', models.BooleanField(default=False)),
            ],
        ),
    ]
