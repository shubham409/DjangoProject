# Generated by Django 4.0.2 on 2022-02-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_auth_perm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(default='Student<django.db.models.fields.AutoField>', max_length=50),
        ),
    ]