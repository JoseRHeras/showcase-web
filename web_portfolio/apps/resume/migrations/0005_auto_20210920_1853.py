# Generated by Django 3.2.6 on 2021-09-20 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20210920_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dutie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.event')),
            ],
        ),
        migrations.DeleteModel(
            name='EventDutie',
        ),
    ]
