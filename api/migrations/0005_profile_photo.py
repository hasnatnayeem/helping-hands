# Generated by Django 2.1.4 on 2018-12-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_donation_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
