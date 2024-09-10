# Generated by Django 5.1.1 on 2024-09-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingIPO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True)),
                ('Price_band', models.IntegerField()),
                ('open_date', models.DateTimeField()),
                ('close_date', models.DateTimeField()),
                ('issue_size', models.IntegerField()),
                ('issue_type', models.CharField(max_length=100)),
                ('listing_date', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
