# Generated by Django 5.0.4 on 2024-05-02 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Promotion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promotion',
            options={'ordering': ['titre']},
        ),
        migrations.AlterModelTable(
            name='promotion',
            table='Promotion',
        ),
    ]
