# Generated by Django 4.1.3 on 2022-11-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='liveurl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
