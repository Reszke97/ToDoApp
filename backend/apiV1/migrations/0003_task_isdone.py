# Generated by Django 3.2.8 on 2022-01-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiV1', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
