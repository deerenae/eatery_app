# Generated by Django 3.0.6 on 2020-05-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=25)),
            ],
        ),
    ]
