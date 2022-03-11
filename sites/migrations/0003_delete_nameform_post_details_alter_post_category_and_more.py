# Generated by Django 4.0.3 on 2022-03-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_nameform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NameForm',
        ),
        migrations.AddField(
            model_name='post',
            name='details',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('------------', '------------'), ('Sport', 'Sport'), ('Politics', 'Politics'), ('Crypto', 'Crypto'), ('Gaming', 'Gaming'), ('Movies', 'Movies'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
