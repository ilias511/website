# Generated by Django 4.0.3 on 2022-03-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_remove_appusername_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='appusername',
            name='age',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
