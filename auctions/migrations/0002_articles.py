# Generated by Django 3.0.8 on 2020-07-10 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('start_bid', models.IntegerField()),
                ('date', models.DateTimeField(default='')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
