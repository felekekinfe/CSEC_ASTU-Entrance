# Generated by Django 4.2.3 on 2023-11-20 00:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("CSEC_APP", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="members",
            name="Roll",
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]