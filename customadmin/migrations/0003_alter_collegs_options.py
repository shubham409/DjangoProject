# Generated by Django 4.0.2 on 2022-02-15 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0002_alter_collegs_options_alter_collegs_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collegs',
            options={'verbose_name': 'College Table'},
        ),
    ]