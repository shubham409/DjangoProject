# Generated by Django 4.0.2 on 2022-02-15 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collegs',
            options={'verbose_name': 'verbose table'},
        ),
        migrations.AlterModelTable(
            name='collegs',
            table='collegs',
        ),
    ]
