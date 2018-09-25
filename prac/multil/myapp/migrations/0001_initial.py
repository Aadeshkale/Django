# Generated by Django 2.1 on 2018-09-25 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Coust',
            fields=[
                ('emp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.Emp')),
                ('email', models.EmailField(max_length=20)),
                ('address', models.CharField(max_length=20)),
            ],
            bases=('myapp.emp',),
        ),
        migrations.CreateModel(
            name='Std',
            fields=[
                ('coust_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.Coust')),
                ('fees', models.IntegerField()),
            ],
            bases=('myapp.coust',),
        ),
    ]