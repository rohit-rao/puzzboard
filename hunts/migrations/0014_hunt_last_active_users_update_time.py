# Generated by Django 4.1.4 on 2023-01-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hunts", "0013_huntsettings_active_user_lookback"),
    ]

    operations = [
        migrations.AddField(
            model_name="hunt",
            name="last_active_users_update_time",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]