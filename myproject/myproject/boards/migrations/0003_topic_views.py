# Generated by Django 2.2.4 on 2019-08-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190815_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
