# Generated by Django 4.1.2 on 2022-12-15 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_rename_description_review_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewed_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_service', to='web.service'),
        ),
    ]