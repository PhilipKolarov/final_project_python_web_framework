# Generated by Django 4.1.2 on 2022-12-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_alter_announcement_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(),
        ),
    ]
