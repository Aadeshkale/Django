# Generated by Django 2.1 on 2018-09-26 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emp',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelTable(
            name='emp',
            table='Employee',
        ),
    ]
