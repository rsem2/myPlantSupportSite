# Generated by Django 4.2.8 on 2023-12-26 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reportPlantStatus", "0003_alter_comment_post_alter_plant_reservoir"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="post", new_name="plant",
        ),
    ]