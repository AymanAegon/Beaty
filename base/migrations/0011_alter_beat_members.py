# Generated by Django 4.0.3 on 2022-03-22 11:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_beat_creater_alter_beat_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='members',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
