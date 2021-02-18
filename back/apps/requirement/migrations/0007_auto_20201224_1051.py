# Generated by Django 3.1.4 on 2020-12-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("requirement", "0006_auto_20201223_2102"),
    ]

    operations = [
        migrations.AddField(
            model_name="requirement",
            name="summary",
            field=models.TextField(default="", max_length=512, verbose_name="Summary"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="requirement",
            name="summary_en",
            field=models.TextField(max_length=512, null=True, verbose_name="Summary"),
        ),
        migrations.AddField(
            model_name="requirement",
            name="summary_ru",
            field=models.TextField(max_length=512, null=True, verbose_name="Summary"),
        ),
    ]