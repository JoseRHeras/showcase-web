# Generated by Django 3.2.6 on 2021-09-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_skill_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='period_range',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]