# Generated by Django 3.2.6 on 2021-09-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_rename_dutie_duty'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=50)),
                ('graduation_date', models.CharField(max_length=20)),
            ],
        ),
    ]
