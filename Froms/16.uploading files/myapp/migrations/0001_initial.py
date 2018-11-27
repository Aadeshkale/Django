# Generated by Django 2.1 on 2018-11-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document', models.FileField(max_length=255, upload_to='media')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
