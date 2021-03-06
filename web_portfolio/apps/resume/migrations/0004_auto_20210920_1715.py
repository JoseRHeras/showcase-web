# Generated by Django 3.2.6 on 2021-09-20 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210920_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='User Name', max_length=70)),
                ('location', models.CharField(default='Chicago', max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('objective', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
