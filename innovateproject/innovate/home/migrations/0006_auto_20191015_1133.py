# Generated by Django 2.2.5 on 2019-10-15 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191015_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='home.Supervisor'),
        ),
    ]
