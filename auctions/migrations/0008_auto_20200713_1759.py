# Generated by Django 3.0.8 on 2020-07-13 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20200713_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='User',
            new_name='user',
        ),
    ]
