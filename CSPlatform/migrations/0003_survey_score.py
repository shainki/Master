# Generated by Django 3.0.6 on 2020-05-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSPlatform', '0002_remove_survey_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='Score',
            field=models.IntegerField(null=True),
        ),
    ]
