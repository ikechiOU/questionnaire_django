# Generated by Django 2.0.1 on 2018-03-02 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pams', '0003_auto_20180302_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='pamsanswer',
            name='team_1',
            field=models.CharField(blank=True, max_length=10, verbose_name='text'),
        ),
        migrations.AddField(
            model_name='pamsanswer',
            name='team_2',
            field=models.CharField(blank=True, max_length=10, verbose_name='text'),
        ),
    ]
