# Generated by Django 2.1.4 on 2018-12-12 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collected_at', models.DateTimeField()),
                ('logged_at', models.DateTimeField(auto_now_add=True)),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile')),
            ],
        ),
    ]
