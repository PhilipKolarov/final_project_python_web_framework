# Generated by Django 4.1.2 on 2022-12-17 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_review_date_alter_service_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='date_sent',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 9, 6, 34, 972093, tzinfo=datetime.timezone.utc)),
        ),
    ]
