# Generated by Django 4.2.8 on 2023-12-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reportPlantStatus", "0004_rename_post_comment_plant"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservoir",
            name="reservoir_status",
            field=models.IntegerField(
                choices=[
                    (1, "Brilliant"),
                    (2, "Good"),
                    (3, "OK"),
                    (4, "Bad"),
                    (5, "Dead"),
                    (6, "Missing"),
                ],
                default=3,
            ),
        ),
    ]
