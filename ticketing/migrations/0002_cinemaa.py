# Generated by Django 3.1.5 on 2021-01-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinemaa',
            fields=[
                ('cinema_code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(default='تهران', max_length=30)),
                ('capacity', models.IntegerField()),
                ('phone', models.CharField(max_length=20, null=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
