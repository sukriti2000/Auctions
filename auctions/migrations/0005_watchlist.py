# Generated by Django 3.0.8 on 2020-07-13 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Article', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.Articles')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='my_watchlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]