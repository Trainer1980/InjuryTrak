# Generated by Django 2.2 on 2020-01-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('injury_app', '0003_auto_20200130_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='sport',
            field=models.CharField(choices=[('Archery', 'Archery'), ('B-Basketball', 'B-Basketball'), ('G-Basketball', 'G-Basketball'), ('Baseball', 'Baseball'), ('B-XCountry', 'B-XCountry'), ('G-XCountry', 'G-XCountry'), ('Football', 'Football'), ('Golf', 'Golf'), ('Gymnastics', 'Gymnastics'), ('B-Soccer', 'B-Soccer'), ('G-Soccer', 'G-Soccer'), ('Softball', 'Softball'), ('Swimming', 'Swimming'), ('Tennis', 'Tennis'), ('B-Track', 'B-Track'), ('G-Track', 'G-Track'), ('Volleyball', 'Volleyball'), ('Wrestling', 'Wrestling')], default='Select_Injury_Site', max_length=45),
        ),
    ]
