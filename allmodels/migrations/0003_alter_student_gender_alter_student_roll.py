# Generated by Django 4.0.2 on 2022-02-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allmodels', '0002_student_remove_allfields_filepath_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male'), ('u', 'undisclosed')], default='Please Enter Gender', max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=10),
        ),
    ]
