# Generated by Django 3.2.1 on 2021-07-02 10:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('software', '0005_auto_20210701_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
