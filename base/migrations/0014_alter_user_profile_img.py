# Generated by Django 4.0.3 on 2022-03-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to='images/'),
        ),
    ]
