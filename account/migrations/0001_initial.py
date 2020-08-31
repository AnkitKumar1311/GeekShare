# Generated by Django 3.1 on 2020-08-31 07:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(default='default.png', upload_to='images/%Y/%m')),
                ('location', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True, null=True)),
                ('joined_on', models.DateTimeField(default=datetime.datetime(2020, 8, 31, 7, 11, 32, 470615, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]