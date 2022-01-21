# Generated by Django 3.2.8 on 2022-01-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiV1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('deadline', models.CharField(blank=True, max_length=255)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
