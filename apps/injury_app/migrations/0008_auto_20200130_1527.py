# Generated by Django 2.2 on 2020-01-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('injury_app', '0007_auto_20200130_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='inj_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='poss_return',
            field=models.DateTimeField(null=True),
        ),
    ]
