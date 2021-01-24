# Generated by Django 3.1.5 on 2021-01-21 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_cinemaa'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('salable_seats', models.IntegerField()),
                ('free_saets', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'فروش شروع نشده است'), (2, 'در حال فروش بلیط'), (3, 'بلیط تمام شد'), (4, 'فروش بلیط بسته شد'), (5, 'فیلم پخش شد'), (6, 'سانس لغو شد')])),
                ('cinemaa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.cinemaa')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.movie')),
            ],
        ),
    ]