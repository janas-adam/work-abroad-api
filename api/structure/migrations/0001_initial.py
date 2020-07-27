# Generated by Django 3.0.8 on 2020-07-27 10:06

import datetime
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('attachment', models.FileField(help_text='attach your cv', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('start_date', models.DateField(default=datetime.date(2020, 7, 27))),
                ('finish_date', models.DateField(default=datetime.date(2020, 7, 27))),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OfferReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('review', models.PositiveSmallIntegerField(help_text="Select review from 1 to 10. '1' is the smallest one.")),
            ],
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('review', models.PositiveSmallIntegerField(help_text="Select review from 1 to 10. '1' is the smallest one.")),
            ],
        ),
    ]
